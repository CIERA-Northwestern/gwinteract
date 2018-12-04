from django.shortcuts import render
from django.http import HttpResponse

from .forms import WaveformForm
# Create your views here.

def index(request):
    form = WaveformForm()
    return render(request, 'waveform-form.html', {'form': form})

def waveforms(request):
    # if this is a POST request we need to process the form data
    if request.method == 'GET':

        # create a form instance and populate it with data from the request:
        form = WaveformForm(request.GET)
        # check whether it's valid:
        if form.is_valid():
           # This is where waveform generation code will go Chris P
           # You parse the request for as such
            m1 = form.cleaned_data['m1']
            m2 = form.cleaned_data['m2']
            print(m1,m2)
            return HttpResponse("M1 is {0}, M2 is {1}".format(m1,m2))
