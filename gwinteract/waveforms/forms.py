from django import forms

from collections import OrderedDict

import lalsimulation

def _is_useable_psd(func):
    try:
        func(0.)
        return True
    except TypeError:
        pass

    return False

def _get_psds(module):
    psds = [[p, getattr(module, p)] for p in dir(module) if "SimNoisePSD" in p]
    psds = [[n, p] for n, p in psds if _is_useable_psd(p)]
    return psds

class WaveformForm(forms.Form):

    _PSDS = OrderedDict(_get_psds(lalsimulation))
    _REPR = OrderedDict((("time", "time domain"),
             ("freq", "frequency domain"),
             ("tf", "time-frequency")))

    representation = forms.ChoiceField(label="representation", \
                            choices=_REPR.items())

    m1 = forms.FloatField(label='m1')#, default=1.4)
    m2 = forms.FloatField(label='m2')#, default=1.4)

    choices = [(p, p) for p in _PSDS.keys()]
    choices.insert(0, ("None", "None"))
    psd = forms.ChoiceField(label="PSD", choices=choices)
