from django import forms
from sqlalchemy.engine import create_engine
from gwpy.table import EventTable

import os
import pandas

class PosteriorForm(forms.Form):

    engine = create_engine("""postgresql://{0}:{1}@gwsci.ciera.northwestern.edu:5432/gw_posteriors""".format(os.environ['GWSCI_USER'], os.environ['GWSCI_PASSWORD']))
    SAMPLE_CHOICES = tuple(zip(engine.table_names(), engine.table_names()))
    parameters_in_table = pandas.read_sql(engine.table_names()[0], engine).keys()
    engine.dispose()
    PARAMETER_CHOICES = tuple(zip(parameters_in_table, parameters_in_table))

    graceid = forms.ChoiceField(choices=SAMPLE_CHOICES,
                                label='Name of Gravitational Wave or SuperEvent ID',
                                )

    param1 = forms.ChoiceField(choices=PARAMETER_CHOICES,)
    param2 = forms.ChoiceField(choices=PARAMETER_CHOICES,)

    param1_min = forms.FloatField(label='parameter 1 min')
    param1_max = forms.FloatField(label='parameter 1 max')
    param2_min = forms.FloatField(label='parameter 2 min')
    param2_max = forms.FloatField(label='parameter 2 max')


def get_min_max_param_json(param, graceid):
    engine = create_engine("""postgresql://{0}:{1}@gwsci.ciera.northwestern.edu:5432/gw_posteriors""".format(os.environ['GWSCI_USER'], os.environ['GWSCI_PASSWORD']))
    ps = pandas.read_sql('SELECT min(\"{0}\"), max(\"{0}\") FROM \"{1}\"'.format(param, graceid), engine)
    engine.dispose()
    return ps.to_json(orient='records')
