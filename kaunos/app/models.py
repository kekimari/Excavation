from django.db import models

class Area(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Trench(models.Model):
    name = models.CharField(max_length=250)
    editor = models.CharField(max_length=250)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)

    # TODO: Add support for files

    def __str__(self):
        return self.name
