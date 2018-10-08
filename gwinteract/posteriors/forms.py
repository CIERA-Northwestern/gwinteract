from django import forms

class PosteriorForm(forms.Form):

    M1 = 'm1'
    M2 = 'm2'
    A1 = 'a1'
    A2 = 'a2'
    DIST = 'dist'
    RA = 'ra'
    DEC = 'dec'

    PARAMETER_CHOICES = (
        (M1, 'm1'),
        (M2, 'm2'),
        (A1, 'a1'),
        (A2, 'a2'),
        (DIST, 'dist'),
        (RA, 'dec'),
        (DEC, 'ra'),
    )

    param1 = forms.ChoiceField(choices=PARAMETER_CHOICES,)
    param2 = forms.ChoiceField(choices=PARAMETER_CHOICES,)
    graceid = forms.CharField(label='Name of Gravitational Wave or SuperEvent ID', max_length=100)
    param1_min = forms.FloatField(label='parameter 1 min')
    param1_max = forms.FloatField(label='parameter 1 max')
    param2_min = forms.FloatField(label='parameter 2 min')
    param2_max = forms.FloatField(label='parameter 2 max')
