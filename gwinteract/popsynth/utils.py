# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import seaborn
"""
seaborn.set(rc={
        # latex
        'text.usetex': True,

        # fonts
        'font.family': 'serif',
        #'font.serif': 'Palatino',
        #'font.sans-serif': 'Helvetica',
        #'font.monospace': 'Ubunto Mono',

        # figure and axes
        'figure.figsize': (10, 10),
        'figure.titlesize': 35,
        'axes.grid': True,
        'axes.titlesize':35,
        #'axes.labelweight': 'bold',
        'axes.labelsize': 30,

        # tick markers
        'xtick.direction': 'in',
        'ytick.direction': 'in',
        'xtick.labelsize': 25,
        'ytick.labelsize': 25,
        'xtick.major.size': 10.0,
        'ytick.major.size': 10.0,
        'xtick.minor.size': 3.0,
        'ytick.minor.size': 3.0,

        # legend
        'legend.fontsize': 20,
        'legend.frameon': True,
        'legend.framealpha': 0.5,

        # colors
        'image.cmap': 'viridis',

        # saving figures
        'savefig.dpi': 150
        }
)
"""

import pandas
import io
import os

from sqlalchemy.engine import create_engine

def histogram_from_form(form):
    # display BNS
    bcm = get_bcm_from_form(form)
    plotting_param1 = form.cleaned_data['plotting_param1']
    plotting_param2 = form.cleaned_data['plotting_param2']
    with seaborn.axes_style('white'):
        plot = seaborn.jointplot(bcm[plotting_param1].values, bcm[plotting_param2].values, kind='scatter', s=8).set_axis_labels(plotting_param1.replace('_', ' '), plotting_param2.replace('_', ' '))
    # make figure able to display in browse
    fig = plot.fig
    return fig

def get_bcm_from_form(form):
    model = form.cleaned_data['model']
    table = form.cleaned_data['table']
    merger_type = form.cleaned_data['merger_type'] 
    plotting_param1 = form.cleaned_data['plotting_param1']
    plotting_param2 = form.cleaned_data['plotting_param2']
    engine = create_engine("""postgresql://{0}:{1}@gwsci.ciera.northwestern.edu:5432/cosmic""".format(os.environ['GWSCI_USER'], os.environ['GWSCI_PASSWORD']))
    bcm = pandas.read_sql('SELECT \"{0}\", \"{1}\" FROM \"{2}\".{3} WHERE merger_type = \'{4}\''.format(plotting_param1, plotting_param2, model, table, merger_type),
                          engine)
    bpp_columns = pandas.read_sql('SELECT * FROM \"{0}\".bpp LIMIT 1'.format(model), engine).keys()
    if (plotting_param1 in bpp_columns) and (plotting_param2 in bpp_columns) and (merger_type != '-001'):
        # Then this person *really* wants to be plotting properties of the system right before it merged
        kstar_type_to_search = (int(merger_type[0:2]), int(merger_type[2:4]))
        bcm = pandas.read_sql('SELECT \"{0}\", \"{1}\" FROM \"{2}\".{3} WHERE kstar_1 IN {4} AND kstar_2 IN {4} AND evol_type =3'.format(plotting_param1, plotting_param2, model, 'bpp', kstar_type_to_search), engine)
    engine.dispose()

    return bcm
