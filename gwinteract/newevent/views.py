from django.shortcuts import render, redirect
from django.http import JsonResponse

# Create your views here.
from .forms import GWEventForm
from .models import GWEvent

from ligo.gracedb.rest import GraceDb

def index(request):
    form = GWEventForm()
    return render(request, 'gw-event-form.html', {'form': form})

def newevent(request):
    # if this is a GET request we need to process the form data
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        form = GWEventForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
           # This is where waveform generation code will go Chris P
           # You parse the request for as such
            superevent_id = str(form.cleaned_data['superevent_id'])
            client = GraceDb("https://gracedb-playground.ligo.org/api/")
            sevent = client.superevent(superevent_id)
            info = sevent.json()
            gwevent, created = GWEvent.objects.get_or_create(superevent_id=superevent_id,
                                                             preferred_event=info['preferred_event'])
            gevent = client.event(info['preferred_event'])
            
            if created:
                if info['gw_id']:
                    gwevent.gw_id = info['gw_id']
                    gwevent.save()
            else:
                if not gwevent.posteriors_uploaded:
                    print("Yep this is here")
                if not gwevent.redshift_uploaded:
                    print("Yep this is here")
                if not gwevent.skymap_uploaded:
                    print("Yep this is here")
            import pdb
            pdb.set_trace()
            return render(request)
