from django import forms

class PopSynthForm(forms.Form):

    MODEL1 = 'model1'

    PARAMETER_CHOICES = (
        (MODEL1, 'model1'),
    )

    model = forms.ChoiceField(choices=PARAMETER_CHOICES,)
