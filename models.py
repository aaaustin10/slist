from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
  users = models.ManyToManyField(User)
  group_name = models.CharField(max_length=30)

class List(models.Model):
  owner = models.ForeignKey(User)
  name = models.CharField(max_length=30)
  groups = models.ManyToManyField(Group)

class Item(models.Model):
  quantity = models.FloatField()
  unit_cost = models.FloatField()
  name = models.CharField(max_length=30)
  units = models.IntegerField()
  lyst = models.ForeignKey(List)

