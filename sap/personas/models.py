from django.db import models



class Persona(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    salario = models.CharField(max_length=255)
    horas_trabajadas = models.CharField(max_length=255)
    

    def __str__(self):
        return f'Persona {self.id}: {self.nombre} {self.apellido} {self.salario} {self.horas_trabajadas}'