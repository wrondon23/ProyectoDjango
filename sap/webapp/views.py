from django.shortcuts import render
from django.http import HttpResponse
from Personas.models import Personas


def index(request):
    personas = Personas.objects.count()
    allPersonas = Personas.objects.all()
    return render(request, 'index.html', {'no_personas': personas, 'allpersonas': allPersonas })

