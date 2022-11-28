from django.db import models

# Create your models here.

class Ingrediente(models.Model):
    nombre= models.CharField(max_length=50)
    def __str__(self):
        return f"id={self.id}, nombre={self.nombre}"
    descripcion=models.CharField(max_length=1024) # o más incluso



class Masa(models.Model):
    nombre= models.CharField(max_length=50)
    precio= models.IntegerField(default=1)
    def __str__(self):
        return f"id={self.id}, nombre={self.nombre}"
    descripcion=models.CharField(max_length=1024) # o más incluso


class Pizza(models.Model):
    nombre= models.CharField(max_length=50)
    def __str__(self):
        return f"id={self.id}, nombre={self.nombre}"
    descripcion=models.CharField(max_length=1024) # o más incluso
    #Relacion many-to-many con los ingredientes
    ingredientes = models.ManyToManyField(Ingrediente, related_name='pizzas')
    #Relacion one-to-many con las masas
    masa = models.ForeignKey(Masa,related_name='pizzas', on_delete=models.CASCADE)
    precio = models.IntegerField(default=0)

