from __future__ import unicode_literals

from django.db import models
from django.core.validators import *

from django.contrib.auth.models import User, Group

from django.contrib import admin
import base64

class Event(models.Model):
    eventtype = models.CharField(max_length=1000, blank=False)
    timestamp = models.DateTimeField()
    userid = models.CharField(max_length=1000, blank=True)
    requestor = models.GenericIPAddressField(blank=False)

    def __str__(self):
        return str(self.eventtype)

class EventAdmin(admin.ModelAdmin):
    list_display = ('eventtype', 'timestamp')

class ApiKey(models.Model):
    owner = models.CharField(max_length=1000, blank=False)
    key = models.CharField(max_length=5000, blank=False)

    def __str__(self):
        return str(self.owner) + str(self.key)

class ApiKeyAdmin(admin.ModelAdmin):
    list_display = ('owner','key')

INT_RATINGS_VALUES = [(it, it) for it in range(1, 6)]

SIZE_CHOICES = [(0, "Tiny"),
        (1, "Small"),
        (2, "Medium"),
        (3, "Large")]

class Breed(models.Model):
    name = models.CharField(max_length=1000, blank=False)
    size = models.CharField(max_length=1000, blank=False, choices=SIZE_CHOICES)
    friendliness = models.IntegerField(choices=INT_RATINGS_VALUES)
    trainability = models.IntegerField(choices=INT_RATINGS_VALUES)
    shedding_amount = models.IntegerField(choices=INT_RATINGS_VALUES)
    exercise_needs = models.IntegerField(choices=INT_RATINGS_VALUES)

class Dog(models.Model):
    name = models.CharField(max_length=1000, blank=False)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.SET_NULL, null=True)
    gender = models.CharField(max_length=20, blank=False)
    color = models.CharField(max_length=1000, blank=False)
    favorite_food = models.CharField(max_length=1000, blank=False)
    favorite_toy = models.CharField(max_length=1000, blank=False)

