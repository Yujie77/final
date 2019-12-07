from django.shortcuts import render
from django.http import HttpResponse
from .forms import SquirrelForm
from django.shortcuts import redirect
from .models import squirrel

def all_squirrels(request):
    squirrels = squirrel.objects.all()
    context = {
        'squirrels': squirrels,
    }
    return render(request, 'sightings/all.html', context)

def add_squirrel(request):
    if request.method == 'POST':
        form = SquirrelForm(request.POST)
        # check data with form
        if form.is_valid():
            form.save()
            return redirect(f'/sightings')
    else:
        form = SquirrelForm()

    context = {
        'form': form,
        'jazz': True,
    }

    return render(request, 'sightings/edit.html', context)

def edit_squirrel(request, squirrel_id):
    getsquirrel= squirrel.objects.get(uniqueid=squirrel_id)
    if request.method == 'POST':
        form = SquirrelForm(request.POST, instance=getsquirrel)
        # check data with form
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/{squirrel_id}')
    else:
        form = SquirrelForm(instance=getsquirrel)

    context = {
        'form': form,
    }

    return render(request, 'sightings/edit.html', context)

def stats_squirrel(request):
    squirrels = squirrel.objects.all()
    context = {
        'squirrels': squirrels,
    }
    return render(request, 'sightings/stats.html', context)
#def index(request):
   # return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.
