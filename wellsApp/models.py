from django.db import models

# Create your models here.


class Well(models.Model):
    name = models.CharField(max_length=100)
    pressureValue = models.FloatField(default=0.0)
    temperatureValue = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
