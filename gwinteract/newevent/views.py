from django.shortcuts import render, redirect
from django.http import JsonResponse

# Create your views here.
from .forms import GWEventForm
from .models import GWEvent

from ligo.gracedb.rest import GraceDb
from sqlalchemy.engine import create_engine

import pandas
import os

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
                return render(request, 'success.html', {'message' : "This event was created"})
            else:
                if not gwevent.posteriors_uploaded:
                    filenames = client.files(gwevent.preferred_event).json()
                    # find posterior samples file
                    post_files = [ifile for ifile in filenames.keys() if 'posterior' in ifile and ',' not in ifile]
                    if len(post_files) == 0:
                        return render(request, 'success.html', {'message' : "No posterior files linked to event"})
                    #download files
                    for ifile in post_files:
                        r = client.files(gwevent.preferred_event, '{0}'.format(ifile))
                        outfile = open('{0}'.format(ifile), 'wb')
                        outfile.write(r.read())
                        outfile.close()
                        try:
                            samples = pandas.read_hdf('{0}'.format(ifile))
                        except:
                            samples = pandas.read_table('{0}'.format(ifile), sep=' ') 

                        engine = create_engine("""postgresql://{0}:{1}@gwsci.ciera.northwestern.edu:5432/gw_posteriors""".format(os.environ['GWSCI_USER'], os.environ['GWSCI_PASSWORD']))
                        samples.to_sql('{0}_{1}'.format(gwevent.superevent_id, ifile.split('.')[0]), engine)
                    gwevent.posteriors_uploaded = True
                    gwevent.save()
                if not gwevent.redshift_uploaded:
                    print("Yep this is here")
                if not gwevent.skymap_uploaded:
                    print("Yep this is here")
                return render(request, 'success.html', {'message' : "This event was updated"})
