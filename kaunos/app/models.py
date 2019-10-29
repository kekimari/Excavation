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

class Building(models.Model):
    name = models.CharField(max_length=250)
    editor = models.CharField(max_length=250)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    date = models.DateTimeField()
    description = models.TextField()
    width = models.FloatField(default=0)
    height = models.FloatField(default=0)
    depth = models.FloatField(default=0)


    # TODO: Add support for files

    def __str__(self):
        return self.name


class Find(models.Model):
    inventory_number = models.IntegerField(default=0)
    depository = models.CharField(max_length=250)
    material = models.CharField(max_length=250)
    description = models.TextField(default='')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    width = models.FloatField(default=0)
    height = models.FloatField(default=0)
    depth = models.FloatField(default=0)
    date = models.DateTimeField()

    # TODO: Add support for files

    def __str__(self):
        return self.inventory_number


class Finding(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    width = models.FloatField(default=0)
    height = models.FloatField(default=0)
    date = models.DateTimeField()


    def __str__(self):
        return self.name

