from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    users = models.ManyToManyField(User)
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

class List(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=30)
    group = models.ManyToManyField(Group)

    def __unicode__(self):
        return self.name

class Item(models.Model):
    quantity = models.FloatField()
    unit_cost = models.FloatField()
    name = models.CharField(max_length=30)
    units = models.IntegerField()
    parent = models.ForeignKey(List)

    def __unicode__(self):
        return self.name

