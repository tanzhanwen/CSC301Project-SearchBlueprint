from django.db import models

class Users(models.Model):
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
class Glossary(models.Model):
    term = models.CharField(unique = True)
    definition = models.TextField()
class DomainName(models.Model):
	id = models.AutoField(primary_key=True)
    domain_name = models.TextField(unique = True)
class Address(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.TextField
    url = models.TextField(unique = True)
    domain = models.ForeignKey
    error = models.IntegerField
    old_rank = models.IntegerField
    new_rank = models.IntegerField
    key_word = models.TextField
    description = models.TextField
    score = models.IntegerField


# Create your models here.
