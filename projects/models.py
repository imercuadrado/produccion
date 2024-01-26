from django.db import models

# Create your models here.

class proyecto(models.Model):
    titulo=models.CharField(max_length=200)
    descripcion=models.TextField()
    tecnologia=models.CharField(max_length=200)
    creado_fecha=models.DateTimeField(auto_now_add=True)

