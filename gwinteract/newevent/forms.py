from django import forms
from django.utils.translation import gettext_lazy as _

from .models import GWEvent
from ligo.gracedb.rest import GraceDb, HTTPError

# Create your models here.
class GWEventForm(forms.ModelForm):
    class Meta:
        model = GWEvent
        fields = ['superevent_id']

        labels = {
            'superevent_id': _("This is the SuperEvent GraceDB ID "
                               "See here: https://gracedb.ligo.org/documentation/models.html#date-based-ids "
                               "for naming conventions."),
        }

    PLAYGROUND = "https://gracedb-playground.ligo.org/api/"
    PRODUCTION = "https://gracedb.ligo.org/api/"

    API_CHOICES = (
        (PLAYGROUND, 'https://gracedb-playground.ligo.org/api/'),
        (PRODUCTION, 'https://gracedb.ligo.org/api/'),
    )
    api = forms.ChoiceField(choices=API_CHOICES,)

    def clean(self):
        cleaned_data = super(GWEventForm, self).clean()
        superevent_id = str(cleaned_data.get('superevent_id'))
        api = str(cleaned_data.get('api'))
        client = GraceDb(api)
        try:
            r = client.ping()
        except HTTPError as e:
            raise forms.ValidationError("Cannot connect to selected "
                                        "api."
                                        )
        try:
            client.superevent(superevent_id)
        except HTTPError as e:
            raise forms.ValidationError(_("Either this super event does not exist, or is not found on  %(value)s"),params={'value': api},)
