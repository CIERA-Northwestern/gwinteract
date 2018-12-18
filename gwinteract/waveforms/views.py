from django.shortcuts import render
from django.http import HttpResponse

from .forms import WaveformForm
# Create your views here.

import io

import numpy
import matplotlib
matplotlib.rc("text", usetex = True)
#matplotlib.use("agg")
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
    psd = map(form._PSDS[name], freq_ar)
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

        # create a form instance and populate it with data from the request:
        form = WaveformForm(request.GET)
        # check whether it's valid:
        if form.is_valid():
           # This is where waveform generation code will go Chris P
           # You parse the request for as such
            f, hp, hx = gen_waveform(form.cleaned_data)
            assert len(f) == len(hp), "{0}, {1}".format(len(f), len(hp))

            asd = gen_psd(form, f) if form.cleaned_data["psd"] != "None" else None

            fig = pyplot.Figure()
            canvas = FigureCanvas(fig)
            ax = fig.add_subplot(1, 1, 1)

            # For now just plot |h|
            # FIXME: These will most likely overlap
            ax.plot(f, numpy.abs(hx), color='red', label=r"$|h_{\times}|(f)$")
            ax.plot(f, numpy.abs(hp), color='black', linestyle='-.', \
                        label=r"$|h_+|(f)$")

            # FIXME: assumes flow is 10 Hz
            idx = numpy.searchsorted(f, 10)
            yscale = max(numpy.abs(hx)[idx], numpy.abs(hp)[idx]) * 1.1

            if asd is not None:
                yscale = max(yscale / 1.1, asd[idx]) * 1.1
                ax.plot(f, asd, color='blue', label=r"$\sqrt{S_n(f)}$")

            ax.set_xlabel(r"Frequency [Hz]")
            ax.set_ylabel(r"Strain [$\textrm{Hz}^{-1/2}$]")

            ax.loglog()
            ax.set_xlim(10, f[-1])
            # FIXME: Set from wf considerations (e.g. amp at isco)
            #pyplot.ylim(1e-25, 1e-23)
            ax.set_ylim(None, yscale)

            fig.legend()
            pyplot.tight_layout()

            buf = io.BytesIO()
            canvas.print_png(buf)
            response = HttpResponse(buf.getvalue(), content_type='image/png')
            fig.clear()
            return response
