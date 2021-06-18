from django.contrib import admin

# Register your models here.
from Personas.models import Personas, Domicilio

admin.site.register(Personas)
admin.site.register(Domicilio)

