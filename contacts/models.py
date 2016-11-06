from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Person(models.Model):
    nickname = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=200)
    birth_date = models.DateField("Birthdate", null=1)
    email = models.CharField(max_length=200)
    activated = models.BooleanField(default=1)

    def __str__(self):
        return self.nickname


class SocialNetwork(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    media = models.CharField(max_length=100)
    url = models.CharField(max_length=500)
    activated = models.BooleanField(default=1)

    def __str__(self):
        return self.media
