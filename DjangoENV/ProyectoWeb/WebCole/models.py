from django.db import models

class Alumno(models.Model):
    
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.IntegerField()
    f_nac=models.DateField(null=True, blank=True, help_text="aqui debe ingresar la fecha de nacimiento")
    direccion=models.CharField(max_length=200)
    legajo = models.IntegerField()
    tel = models.CharField(max_length=200)
    curso = models.CharField(max_length=200)

    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p. ej. en el sitio de Administración)
        """
        return '%s %s %s' %(self.apellido, self.nombre, self.dni)


    