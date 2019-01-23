# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'index.html')

def index(request):
    return redirect('/home')
