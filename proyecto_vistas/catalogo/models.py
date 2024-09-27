from django.db import models

# Create your models here.

#creamos el modelo de pais
#Tiene dos atributos (nombre y codigo)
class Pais(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre
    

