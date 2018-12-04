from django import forms

class WaveformForm(forms.Form):

    m1 = forms.FloatField(label='m1')
    m2 = forms.FloatField(label='m2')
