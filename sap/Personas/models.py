from django.db import models


# Create your models here.
class Domicilio(models.Model):
    calle = models.CharField(max_length=255)
    numero_calle = models.IntegerField()
    pais = models.CharField(max_length=255)

    def __str__(self):
        return f'Domicilio {self.id} : {self.calle} {self.numero_calle} {self.pais} '

class Personas(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    domicilio = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Personas {self.id}: {self.nombre} {self.apellido} {self.email}'
