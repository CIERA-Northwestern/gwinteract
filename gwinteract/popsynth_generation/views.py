from django.shortcuts import render

# Create your views here.
from .forms import NewPopSynthForm
from .models import NewPopSynthModel

def index(request):
    #if request.user.is_authenticated:
        form = NewPopSynthForm()
        return render(request, 'popsynth-generation-form.html', {'form': form})

def population_synthesis_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        form = NewPopSynthForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            # First determine the subjects attempting to be added to the training set
            new_popsynth_model, created = NewPopSynthModel.objects.get_or_create(**form.cleaned_data)
            if not created:
                return render(request, 'success.html', {'message' : "This population has already been run"})

            new_popsynth_model.save()

            return render(request, 'success.html', {'message' : "Your request has successfully been submitted and you should expect an email when it is completed"})
        else:
            return render(request, 'popsynth-generation-form.html', {'form': form})
