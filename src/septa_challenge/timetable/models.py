from django.db import models

class Station(models.Model):
    name = models.CharField(max_length=200)
    lines = models.ManyToManyField('Line')
    fare_zone = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name

class Line(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name
