from django.forms import modelform_factory
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from Personas.models import Personas


def detalle_personas(request, id):
    try:
        personas = Personas.objects.get(pk=id)
        return render(request, 'personas/detalle.html', {'persona': personas})
    except:
        return render(request, 'personas/404.html')


PersonaForm = modelform_factory(Personas, exclude=[])


def nuevaPersona(request):
    formaPersona = PersonaForm()
    return render(request, 'personas/nuevo.html', {'formaPersona': formaPersona})
