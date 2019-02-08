from django import forms

import lalsimulation
import numpy as np

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Fieldset

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
    def __init__(self, *args, **kwargs):
        super(WaveformForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = '/waveforms/plot/'
        self.helper.form_method = 'GET'
        self.helper.form_id = 'waveform_form'
        self.helper.form_style = 'inline'
        self.helper.layout = Layout(
            Fieldset("Intrinsic Parameters",
                Row(
                    Column('m1', css_class='form-group col-md-6 mb-0'),
                    Column('m2', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
                Row(
                    Column('spin1x', css_class='form-group col-md-4 mb-0'),
                    Column('spin1y', css_class='form-group col-md-4 mb-0'),
                    Column('spin1z', css_class='form-group col-md-4 mb-0'),
                    css_class='form-row'
                ),
                Row(
                    Column('spin2x', css_class='form-group col-md-4 mb-0'),
                    Column('spin2y', css_class='form-group col-md-4 mb-0'),
                    Column('spin2z', css_class='form-group col-md-4 mb-0'),
                    css_class='form-row'
                ),
                Row(
                    Column('distance', css_class='form-group col-md-6 mb-0'),
                    Column('inclination', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
                ),
            Fieldset("Power Spectral Density", 'psd'),
            Submit('submit', 'Generate Waveform')
        )

    _PSDS = dict(_get_psds(lalsimulation))

    m1 = forms.FloatField(label='m1')
    m2 = forms.FloatField(label='m2')

    spin1x = forms.FloatField(label='spin1x', min_value=-1.0, max_value=1.0)
    spin1y = forms.FloatField(label='spin1y', min_value=-1.0, max_value=1.0)
    spin1z = forms.FloatField(label='spin1z', min_value=-1.0, max_value=1.0)

    spin2x = forms.FloatField(label='spin2x', min_value=-1.0, max_value=1.0)
    spin2y = forms.FloatField(label='spin2y', min_value=-1.0, max_value=1.0)
    spin2z = forms.FloatField(label='spin2z', min_value=-1.0, max_value=1.0)

    distance = forms.FloatField(label='distance', min_value=0.0)
    inclination = forms.FloatField(label='inclination', min_value=0.0, max_value=np.pi)

    choices = [(p, p) for p in _PSDS.keys()]
    choices.insert(0, ("None", "None"))
    psd = forms.ChoiceField(label="PSD", choices=choices)
