from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import TemplateView

from sightings.models import squirrel

class Home(TemplateView):
    template_name = 'template.html'

#def index(request):
    #return render(request,'map/template.html')

def all_squirrels(request):
    #squirrels = squirrel.objects.all()
    squirrels = squirrel.objects.all()[0:10]
    context = {
        'squirrels': squirrels,
    }
    return render(request, 'map/template.html', context)


