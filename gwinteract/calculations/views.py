# *- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def calculations(request):
    return render(request, 'gw_quick_calc.html')
