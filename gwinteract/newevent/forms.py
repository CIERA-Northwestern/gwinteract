from django import forms
from django.utils.translation import gettext_lazy as _

from .models import GWEvent
from ligo.gracedb.rest import GraceDb

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

    def clean(self):
        cleaned_data = super(GWEventForm, self).clean()
        superevent_id = str(cleaned_data.get('superevent_id'))
        client = GraceDb("https://gracedb-playground.ligo.org/api/")
        try:
            client.superevent(superevent_id)
        except:
            raise forms.ValidationError("Either this super event does not "
                                        "exist, or is not "
                                        "found on gracedb-playground.ligo.org."
                                        )
