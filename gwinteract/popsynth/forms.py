from django import forms
from sqlalchemy.engine import create_engine

import os
import pandas

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Fieldset

class PopSynthForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(PopSynthForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = '/popsynth/plot_bns'
        self.helper.form_method = 'GET'
        self.helper.form_id = 'popsynth_form'
        self.helper.form_style = 'inline'
        self.helper.layout = Layout(
            Fieldset("Model and Table",
                Row(
                    Column('model', css_class='form-group col-md-6 mb-0'),
                    Column('table', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
                ),
            Fieldset("Type of Systems to Display Parameters For",
                Row(
                    Column('bin_state', css_class='form-group col-md-6 mb-0'),
                    Column('merger_type', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
                ),
            Fieldset("Parameters to Display",
                Row(
                    Column('plotting_param1', css_class='form-group col-md-6 mb-0'),
                    Column('plotting_param2', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
                ),
            Submit('submit', 'Plot Population Parameters')
        )

    INITIAL_CONDITIONS = 'initial_conditions'
    BCM = 'bcm'
    BPP = 'bpp'
    TABLE_CHOICES = (
        (BCM, 'bcm'),
        (INITIAL_CONDITIONS, 'initial_conditions'),
        (BPP, 'bpp'),
    )

    engine = create_engine("""postgresql://{0}:{1}@gwsci.ciera.northwestern.edu:5432/cosmic""".format(os.environ['GWSCI_USER'], os.environ['GWSCI_PASSWORD']))

    models = pandas.read_sql('select distinct(table_schema) from information_schema.tables '
                             'where table_schema not in (\'pg_catalog\', \'information_schema\')',
                              engine)
    MODEL_CHOICES = tuple(zip(models.table_schema.values , models.table_schema.values))

    columns = pandas.read_sql('SELECT * FROM \"{0}\".{1} LIMIT 1'.format(MODEL_CHOICES[0][0], TABLE_CHOICES[0][0]), engine).keys()
    COLUMN_CHOICES = tuple(zip(columns, columns))

    binary_state = pandas.read_sql('SELECT DISTINCT(bin_state) FROM \"{0}\".{1}'.format(MODEL_CHOICES[0][0], TABLE_CHOICES[0][0]), engine).bin_state.values
    BINARY_STATE_CHOICES = tuple(zip(binary_state, binary_state))

    merger_types = pandas.read_sql('SELECT DISTINCT(merger_type) FROM \"{0}\".{1}'.format(MODEL_CHOICES[0][0], TABLE_CHOICES[0][0]), engine).merger_type.values
    MERGER_TYPES_CHOICES = tuple(zip(merger_types, merger_types))

    engine.dispose()

    model = forms.ChoiceField(choices=MODEL_CHOICES,)
    table = forms.ChoiceField(choices=TABLE_CHOICES,)
    bin_state = forms.ChoiceField(choices=BINARY_STATE_CHOICES,)
    merger_type = forms.ChoiceField(choices=MERGER_TYPES_CHOICES,)
    plotting_param1 = forms.ChoiceField(choices=COLUMN_CHOICES,)
    plotting_param2 = forms.ChoiceField(choices=COLUMN_CHOICES,)
