from django.db import models

# Create your models here.



class Company(models.Model):
    name = models.CharField(max_length=100)
    isPublisher = models.BooleanField()
    isStudio = models.BooleanField()
    isManufacturer = models.BooleanField()

    def __unicode__(self):
        return self.name
    #votes = models.IntegerField(default=0)

class Platform(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Company, limit_choices_to={'isManufacturer': True})
    def __unicode__(self):
        return self.name


class Game(models.Model):
    publisher = models.ForeignKey(Company, related_name='publisher', limit_choices_to={'isPublisher': True})
    studio = models.ForeignKey(Company, related_name='studio', limit_choices_to={'isStudio': True})
    name = models.CharField(max_length=100)
    shortname = models.CharField(max_length=64)
    published_date = models.DateTimeField('date published')

    platforms = models.ManyToManyField(Platform)
    def __unicode__(self):
        return self.name


