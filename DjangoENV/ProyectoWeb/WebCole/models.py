from django.db import models

class Materia(models.Model):
    
    name = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = "materia"
        verbose_name_plural = "materias"

    def __str__(self):
        return self.name

class Alumno(models.Model):
    
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.IntegerField()
    f_nac=models.DateField(null=True, blank=True, help_text="aqui debe ingresar la fecha de nacimiento")
    direccion=models.CharField(max_length=200)
    legajo = models.IntegerField()
    tel = models.CharField(max_length=200)
    curso = models.CharField(max_length=200)
    Materia = models.ManyToManyField(Materia, verbose_name="Materias")
    """categories = models.ManyToManyField(Category, 
        verbose_name="Categorías")
    """
    class Meta:
        verbose_name = "alumno"
        verbose_name_plural = "alumnos"

    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p. ej. en el sitio de Administración)
        """
        return '%s %s %s' %(self.apellido, self.nombre, self.dni)


    

    