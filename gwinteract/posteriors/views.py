# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render
from .forms import PosteriorForm
from .forms import get_min_max_param_json

from ligo.gracedb.rest import GraceDb, HTTPError
from gwpy.table import EventTable

import seaborn

from matplotlib import use
use('agg')
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

import os

# Create your views here.
def index(request):
    form = PosteriorForm()
    return render(request, 'form.html', {'form': form})

def posteriors(request):
    # if this is a POST request we need to process the form data
    if request.method == 'GET':

        # create a form instance and populate it with data from the request:
        form = PosteriorForm(request.GET)
        # check whether it's valid:
        if form.is_valid():
            ps = filter_and_get_samples(form)
            old = 'posteriors'
            new = 'histogram'
            histogramurl = (request.get_full_path()[::-1].replace(old[::-1], new[::-1], 1))[::-1]

            return render(request, 'gracedb.html', {'results' : ps.to_html(table_id="samples"), 'histogramurl' : histogramurl})
        else:
            return render(request, 'form.html', {'form': form})


def histogram(request):
    # if this is a POST request we need to process the form data
    if request.method == 'GET':

        # create a form instance and populate it with data from the request:
        form = PosteriorForm(request.GET)
        # check whether it's valid:
        if form.is_valid():
            ps = filter_and_get_samples(form) 
            param1 = form.cleaned_data['param1']
            param2 = form.cleaned_data['param2']

            with seaborn.axes_style('white'):
                plot = seaborn.jointplot(param1, param2, ps, kind='kde')

            fig = plot.fig
            canvas = FigureCanvas(fig)

            import io
            buf = io.BytesIO()
            canvas.print_png(buf)
            response=HttpResponse(buf.getvalue(),content_type='image/png')
            fig.clear()
            return response

def filter_and_get_samples(form):
    graceid = form.cleaned_data['graceid']
    param1 = form.cleaned_data['param1']
    param2 = form.cleaned_data['param2']
    param1_min = form.cleaned_data['param1_min']
    param1_max = form.cleaned_data['param1_max']
    param2_min = form.cleaned_data['param2_min']
    param2_max = form.cleaned_data['param2_max']

    ps = EventTable.fetch('gravityspy', '\"{0}\"'.format(graceid),
                          selection=['{0}<{1}<{2}'.format(param1_min, param1, param1_max),
                                     '{0}<{1}<{2}'.format(param2_min, param2, param2_max)],
                          db='gw_posteriors',
                          host='gwsci.ciera.northwestern.edu',
                          user=os.getenv('GWSCI_USER'),
                          passwd=os.getenv('GWSCI_PASSWORD'))
    ps = ps.to_pandas().sample(n=1000)
    return ps

def get_min_max_param(request):
    if request.method == 'GET':
        param = request.GET.get('param', '')
        graceid = request.GET.get('graceid', '')
        data = get_min_max_param_json(param=param, graceid=graceid)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
