from django.db import models

class Users(models.Model):
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
class Glossary(models.Model):
    term = models.CharField(max_length=50)
    definition = models.TextField(blank=True)
class Domain(models.Model):
    name = models.TextField(blank=True)
class Address(models.Model):
    title = models.TextField(blank=True)
    url = models.TextField(blank=True)
    domain = models.ForeignKey(Domain)
    error = models.IntegerField(default=0)
    old_rank = models.IntegerField(default =0)
    new_rank = models.IntegerField(default =0)
    key_word = models.TextField(blank=True)
    description = models.TextField(blank=True)
    score = models.IntegerField(default =0)


# Create your models here.
