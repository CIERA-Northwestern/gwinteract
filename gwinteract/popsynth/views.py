# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render
from .forms import PopSynthForm

import seaborn
seaborn.set(rc={'text.usetex' : False})
import pandas
import io

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
            new = 'plot_nsbh'
            nsbh_plot_url = (request.get_full_path()[::-1].replace(old[::-1], new[::-1], 1))[::-1]
            new = 'plot_bbh'
            bbh_plot_url = (request.get_full_path()[::-1].replace(old[::-1], new[::-1], 1))[::-1]

            return render(request, 'popsynth-results.html',
                          {'bns_plot_url' : bns_plot_url,
                           'nsbh_plot_url' : nsbh_plot_url,
                           'bbh_plot_url' : bbh_plot_url,})
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
            bpp = pandas.read_hdf('dat_FIRE_13_15_13_15.h5', key='/bpp')
            bcm = pandas.read_hdf('dat_FIRE_13_15_13_15.h5', key='/bcm')
            init_cond = pandas.read_hdf('dat_FIRE_13_15_13_15.h5', key='/initCond')
            bns_bcm = bcm.loc[bcm.merger_type ==1313]
            bns_bpp = bpp.loc[bpp.bin_num.isin(bns_bcm.bin_num)]
            bns_init_cond = init_cond.loc[init_cond.bin_num.isin(bns_bcm.bin_num)]

            # find (source frame) masses at time of merger
            systems = bns_bpp.loc[(bns_bpp.kstar_1 == 13) & (bns_bpp.kstar_2 == 13) & (bns_bpp.evol_type == 3)]
            with seaborn.axes_style('white'):
                plot = seaborn.jointplot('mass_1', 'mass_2', systems).set_axis_labels("mass 1", "mass 2")
            # make figure able to display in browser
            fig = plot.fig
            canvas = FigureCanvas(fig)
            buf = io.BytesIO()
            canvas.print_png(buf)
            response=HttpResponse(buf.getvalue(),content_type='image/png')
            fig.clear()
            return response

def plot_nsbh(request):
    # if this is a POST request we need to process the form data
    if request.method == 'GET':

        # create a form instance and populate it with data from the request:
        form = PopSynthForm(request.GET)
        # check whether it's valid:
        if form.is_valid():
            # display BNS
            bpp = pandas.read_hdf('dat_FIRE_13_15_13_15.h5', key='/bpp')
            bcm = pandas.read_hdf('dat_FIRE_13_15_13_15.h5', key='/bcm')
            init_cond = pandas.read_hdf('dat_FIRE_13_15_13_15.h5', key='/initCond')
            nsbh_bcm = bcm.loc[bcm.merger_type.isin([1314,1413])]
            nsbh_bpp = bpp.loc[bpp.bin_num.isin(nsbh_bcm.bin_num)]
            nsbh_init_cond = init_cond.loc[init_cond.bin_num.isin(nsbh_bcm.bin_num)]

            # find (source frame) masses at time of merger
            systems = nsbh_bpp.loc[(nsbh_bpp.kstar_1.isin([14,13])) & (nsbh_bpp.kstar_2.isin([14,13])) & (nsbh_bpp.evol_type == 3)]
            with seaborn.axes_style('white'):
                plot = seaborn.jointplot('mass_1', 'mass_2', systems,).set_axis_labels("mass 1", "mass 2")
            # make figure able to display in browser
            fig = plot.fig
            canvas = FigureCanvas(fig)
            buf = io.BytesIO()
            canvas.print_png(buf)
            response=HttpResponse(buf.getvalue(),content_type='image/png')
            fig.clear()
            return response

def plot_bbh(request):
    # if this is a POST request we need to process the form data
    if request.method == 'GET':

        # create a form instance and populate it with data from the request:
        form = PopSynthForm(request.GET)
        # check whether it's valid:
        if form.is_valid():
            # display BNS
            bpp = pandas.read_hdf('dat_FIRE_13_15_13_15.h5', key='/bpp')
            bcm = pandas.read_hdf('dat_FIRE_13_15_13_15.h5', key='/bcm')
            init_cond = pandas.read_hdf('dat_FIRE_13_15_13_15.h5', key='/initCond')
            bbh_bcm = bcm.loc[bcm.merger_type ==1414]
            bbh_bpp = bpp.loc[bpp.bin_num.isin(bbh_bcm.bin_num)]
            bbh_init_cond = init_cond.loc[init_cond.bin_num.isin(bbh_bcm.bin_num)]

            # find (source frame) masses at time of merger
            systems = bbh_bpp.loc[(bbh_bpp.kstar_1 == 14) & (bbh_bpp.kstar_2 == 14) & (bbh_bpp.evol_type == 3)]
            with seaborn.axes_style('white'):
                plot = seaborn.jointplot('mass_1', 'mass_2', systems,).set_axis_labels("mass 1", "mass 2")
            # make figure able to display in browser
            fig_bbh = plot.fig
            canvas = FigureCanvas(fig_bbh)
            buf = io.BytesIO()
            canvas.print_png(buf)
            response=HttpResponse(buf.getvalue(),content_type='image/png')
            pyplot.close(fig_bbh)
            return response
