from django.shortcuts import render
from django.http import HttpResponse

from .forms import WaveformForm
# Create your views here.

import io

import numpy
from gwpy.frequencyseries import FrequencySeries
from gwpy.timeseries import TimeSeries
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

def gen_waveform_td(event_params, flow=10.0, fhigh=2048.,
                    fref=10., approximant="IMRPhenomPv2"):
    """
    Generate the h_+ and h_x polarizations for an event, as well as an associated frequency array.
    """
    eprm = _defaults.copy()
    eprm.update(event_params)

    delta_t = 0.5 / fhigh

    params = None
    hp, hx = lalsimulation.SimInspiralTD(
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
                delta_t, flow, fref, \
                # Other extraneous options
                params,
                lalsimulation.SimInspiralGetApproximantFromString(approximant))

    time_ar = numpy.arange(0, len(hp.data.data)) * delta_t
    time_ar += float(hp.epoch)

    return time_ar, hp.data.data, hx.data.data

def gen_waveform_fd(event_params, deltaf=0.125, flow=10.0, fhigh=2048.,
                    fref=10., approximant="IMRPhenomPv2"):
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

def plot_fd(form, plot_flow=10., plot_fhigh=2048., ax=None):

    f, hp, hx = gen_waveform_fd(form.cleaned_data)
    assert len(f) == len(hp), "{0}, {1}".format(len(f), len(hp))

    hp = FrequencySeries(hp, frequencies=f)
    hx = FrequencySeries(hx, frequencies=f)

    asd = FrequencySeries(gen_psd(form, f), frequencies=f) if \
                        form.cleaned_data["psd"] != "None" else None

    #if ax is not None:
        #plot.sca(ax)
    plot = hp.abs().plot(color='red', label=r"$|h_+|(f)$", yscale='log')
    ax = plot.gca()
    ax.plot(hx.abs(), color='black', linestyle='-.', label=r"$|h_{\times}|(f)$")
    if asd is not None:
        ax.plot(asd)

    ax.set_xlim(plot_flow, plot_fhigh)

    # For now just plot |h|
    # FIXME: These will most likely overlap
    ax.set_ylabel(r'GW strain [strain$/\sqrt{\mathrm{Hz}}$]')
    plot.legend()
    return plot

def plot_td(form, ax=None):

    t, hp, hx = gen_waveform_td(form.cleaned_data, flow=10)
    assert len(t) == len(hp), "{0}, {1}".format(len(t), len(hp))

    hp = TimeSeries(hp, t0=t[0], dt=t[1] - t[0])
    hx = TimeSeries(hx, t0=t[0], dt=t[1] - t[0])

    #if ax is not None:
        #plot.sca(ax)
    plot = hp.plot(color='red', label=r"$h_+(t)$")
    ax = plot.gca()
    ax.plot(hx, color='black', label=r"$h_{\times}(t)$")

    # For now just plot |h|
    # FIXME: These will most likely overlap
    ax.set_ylabel(r'GW strain [strain]')
    ax.set_xlabel(r'time [s]')
    plot.legend()
    return plot

def plot_tf(form, ax=None):

    t, hp, hx = gen_waveform_td(form.cleaned_data, flow=10)
    assert len(t) == len(hp), "{0}, {1}".format(len(t), len(hp))

    hp = TimeSeries(hp, t0=t[0], dt=t[1] - t[0])
    hx = TimeSeries(hx, t0=t[0], dt=t[1] - t[0])

    q = hp.q_transform()
    med, sig = numpy.median(q), numpy.std(q)

    #if ax is not None:
        #plot.sca(ax)
    plot = q.plot(vmin=(med - 5 * sig))
    ax = plot.gca()
    ax.set_yscale('log')

    return plot

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

            if form.cleaned_data["representation"] == "freq":
                plot = plot_fd(form)
            elif form.cleaned_data["representation"] == "time":
                plot = plot_td(form)
            else:
                plot = plot_tf(form)

            # Package result and export through HTTP response
            buf = io.BytesIO()
            canvas = FigureCanvas(plot)
            canvas.print_png(buf)
            response = HttpResponse(buf.getvalue(), content_type='image/png')
            pyplot.close(plot)
            return response
