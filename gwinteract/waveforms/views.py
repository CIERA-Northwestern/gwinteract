from django.shortcuts import render
from django.http import HttpResponse

from .forms import WaveformForm
# Create your views here.

import io

import numpy
from gwpy.frequencyseries import FrequencySeries
from matplotlib import pyplot
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

####### Waveform Generation
# Adapted from `eventgen.py` in `gw_event_gen`
import lal
import lalsimulation

_defaults = {
    "m1": 1.4, "m2": 1.4,
    "spin1x": 0., "spin1y": 0., "spin1z": 0.,
    "spin2x": 0., "spin2y": 0., "spin2z": 0.,
    "distance": 100., "inclination": 0.,
}

def gen_waveform(event_params, flow=10.0, deltaf=0.125, fhigh=2048., fref=10.,
                    approximant="IMRPhenomPv2"):
    """
    Generate the h_+ and h_x polarizations for an event, as well as an associated frequency array.
    """
    eprm = _defaults.copy()
    eprm.update(event_params)

    freq_ar = numpy.arange(0, fhigh + deltaf, deltaf)
    params = None
    hp, hx = lalsimulation.SimInspiralFD(
                # Masses
                eprm["m1"] * lal.MSUN_SI, eprm["m2"] * lal.MSUN_SI, \
                # Spins
                eprm["spin1x"], eprm["spin1y"], eprm["spin1z"], \
                eprm["spin1x"], eprm["spin1y"], eprm["spin1z"], \
                # distance and inclination
                eprm["distance"] * 1e6 * lal.PC_SI, eprm["inclination"],
                # These are eccentricity and other orbital parameters
                0.0, 0.0, 0.0, 0.0,
                # frequency binning params
                deltaf, flow, fhigh, fref, \
                # Other extraneous options
                params,
                lalsimulation.SimInspiralGetApproximantFromString(approximant))

    return freq_ar, hp.data.data, hx.data.data

def gen_psd(form, freq_ar, asd=True):
    name = form.cleaned_data["psd"]
    psd = list(map(form._PSDS[name], freq_ar))
    # DC component is always set to nan
    psd[0] = psd[1]
    return numpy.sqrt(psd) if asd else numpy.asarray(psd)

#######

def index(request):
    form = WaveformForm()
    return render(request, 'waveform-form.html', {'form': form})

def waveforms(request):
    # if this is a POST request we need to process the form data
    if request.method == 'GET':
        # check whether it's valid:
        form = WaveformForm(request.GET)
        if form.is_valid():
            waveformurl = request.get_full_path()[::-1].replace('waveforms'[::-1], 'plot'[::-1], 1)[::-1]
            return render(request, 'waveform-results.html', {'waveformurl' : waveformurl})
        else:
            return render(request, 'waveform-form.html', {'form': form})

def plot(request):
    # if this is a POST request we need to process the form data
    if request.method == 'GET':

        # create a form instance and populate it with data from the request:
        form = WaveformForm(request.GET)
        # check whether it's valid:
        if form.is_valid():
           # This is where waveform generation code will go Chris P
           # You parse the request for as such
            f, hp, hx = gen_waveform(form.cleaned_data)
            assert len(f) == len(hp), "{0}, {1}".format(len(f), len(hp))

            hp = FrequencySeries(hp, frequencies=f)
            hx = FrequencySeries(hx, frequencies=f)

            asd = FrequencySeries(gen_psd(form, f), frequencies=f) if form.cleaned_data["psd"] != "None" else None

            plot = hp.abs().plot(color='red', label=r"$|h_+|(f)$", yscale='log')
            ax = plot.gca()
            ax.plot(hx.abs(), color='black', linestyle='-.', label=r"$|h_x|(f)$")
            if asd is not None:
                ax.plot(asd)

            # For now just plot |h|
            # FIXME: These will most likely overlap
            ax.set_ylabel(r'GW strain [strain$/\sqrt{\mathrm{Hz}}$]')
            plot.legend()
            buf = io.BytesIO()
            canvas = FigureCanvas(plot)
            canvas.print_png(buf)
            response = HttpResponse(buf.getvalue(), content_type='image/png')
            pyplot.close(plot)
            return response
