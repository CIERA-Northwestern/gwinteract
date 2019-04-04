# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render
from .forms import PopSynthForm
from .utils import get_bcm_from_form,histogram_from_form

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
            fig = histogram_from_form(form)
            canvas = FigureCanvas(fig)
            buf = io.BytesIO()
            canvas.print_png(buf)
            response=HttpResponse(buf.getvalue(),content_type='image/png')
            fig.clear()
            return response
