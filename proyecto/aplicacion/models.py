from django.db import models
from django.utils import timezone


# Create your models here.

class Camion(models.Model):
    nombreC = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        super(Camion, self).save(*args, **kwargs)

    def __str__(self):
        return "Camion: "+self.nombreC

class Objeto(models.Model):
    nombreO = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        super(Objeto, self).save(*args, **kwargs)

    def __str__(self):
        return "Objeto: "+self.nombreO

class Ruta(models.Model):
    camion = models.ForeignKey(Camion, on_delete=models.CASCADE, null=False)
    objeto = models.ForeignKey(Objeto, on_delete=models.CASCADE, null=False)
    fechaDeReparto = models.DateTimeField(blank=False, default=timezone.now)

    def save(self, *args, **kwargs):
        super(Ruta, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.camion)+""+str(self.objeto)