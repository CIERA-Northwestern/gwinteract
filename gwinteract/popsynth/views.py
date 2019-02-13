# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render
from .forms import PopSynthForm

import seaborn
seaborn.set(rc={'text.usetex' : False})
import pandas
import io
import os

from sqlalchemy.engine import create_engine
from matplotlib import use
use('agg')
from matplotlib import pyplot
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

# Create your views here.
def index(request):
    form = PopSynthForm()
    return render(request, 'popsynth-form.html', {'form': form})

def popsynth(request):
    # if this is a POST request we need to process the form data
    if request.method == 'GET':

        # create a form instance and populate it with data from the request:
        form = PopSynthForm(request.GET)
        # check whether it's valid:
        if form.is_valid():
            model = form.cleaned_data['model']
            old = 'popsynth'
            new = 'plot_bns'
            bns_plot_url = (request.get_full_path()[::-1].replace(old[::-1], new[::-1], 1))[::-1]

            return render(request, 'popsynth-results.html',
                          {'bns_plot_url' : bns_plot_url,})
        else:
            return render(request, 'form.html', {'popsynth-form.html': form})

def plot_bns(request):
    # if this is a POST request we need to process the form data
    if request.method == 'GET':

        # create a form instance and populate it with data from the request:
        form = PopSynthForm(request.GET)
        # check whether it's valid:
        if form.is_valid():
            # display BNS
            bcm = get_bcm_from_form(form)
            plotting_param1 = form.cleaned_data['plotting_param1']
            plotting_param2 = form.cleaned_data['plotting_param2']
            with seaborn.axes_style('white'):
                plot = seaborn.jointplot(plotting_param1, plotting_param2, bcm).set_axis_labels(plotting_param1.replace('_', ' '), plotting_param2.replace('_', ' '))
            # make figure able to display in browser
            fig = plot.fig
            canvas = FigureCanvas(fig)
            buf = io.BytesIO()
            canvas.print_png(buf)
            response=HttpResponse(buf.getvalue(),content_type='image/png')
            fig.clear()
            return response


def get_bcm_from_form(form):
    model = form.cleaned_data['model']
    table = form.cleaned_data['table']
    merger_type = form.cleaned_data['merger_type'] 
    plotting_param1 = form.cleaned_data['plotting_param1']
    plotting_param2 = form.cleaned_data['plotting_param2']
    engine = create_engine("""postgresql://{0}:{1}@gwsci.ciera.northwestern.edu:5432/cosmic""".format(os.environ['GWSCI_USER'], os.environ['GWSCI_PASSWORD']))
    bcm = pandas.read_sql('SELECT \"{0}\", \"{1}\" FROM {2}.{3} WHERE merger_type = \'{4}\''.format(plotting_param1, plotting_param2, model, table, merger_type),
                          engine)
    bpp_columns = pandas.read_sql('SELECT * FROM {0}.bpp LIMIT 1'.format(model), engine).keys()
    if (plotting_param1 in bpp_columns) and (plotting_param2 in bpp_columns) and (merger_type != '-001'):
        # Then this person *really* wants to be plotting properties of the system right before it merged
        kstar_type_to_search = (int(merger_type[0:2]), int(merger_type[2:4]))
        bcm = pandas.read_sql('SELECT \"{0}\", \"{1}\" FROM {2}.{3} WHERE kstar_1 IN {4} AND kstar_2 IN {4} AND evol_type =3'.format(plotting_param1, plotting_param2, model, 'bpp', kstar_type_to_search), engine)
    engine.dispose()

    return bcm
