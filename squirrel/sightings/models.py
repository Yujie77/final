from django.db import models

# Create your models here.

class squirrel(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    uniqueid = models.CharField(max_length=150)
    shift = models.CharField(max_length=150,blank=True)
    Date = models.IntegerField(blank=True)
    Age = models.CharField(max_length=150,blank=True)
    furcolor = models.CharField(max_length=150,blank=True)
    location = models.CharField(max_length=150,blank=True)
    specificlocation = models.CharField(max_length=150,blank=True)
    running = models.CharField(max_length=150,blank=True)
    chasing = models.CharField(max_length=150,blank=True)
    climbing = models.CharField(max_length=150,blank=True)
    eating = models.CharField(max_length=150,blank=True)
    foraging = models.CharField(max_length=150,blank=True)
    otheractivities = models.CharField(max_length=150,blank=True)
    kuks = models.CharField(max_length=150,blank=True)
    quaas = models.CharField(max_length=150,blank=True)
    moans = models.CharField(max_length=150,blank=True)
    tailflags = models.CharField(max_length=150,blank=True)
    tailtwitches = models.CharField(max_length=150,blank=True)
    approaches = models.CharField(max_length=150,blank=True)
    indifferent = models.CharField(max_length=150,blank=True)
    runsfrom = models.CharField(max_length=150,blank=True)
    def __str__(self):
        return self.uniqueid
