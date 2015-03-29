from django.db import models

class Users(models.Model):
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
class Glossary(models.Model):
    term = models.CharField(max_length=30)
    definition = models.TextField()
class DomainName(models.Model):
    domain_name = models.CharField(max_length=30)
class Address(models.Model):
    address_name = models.CharField(max_length=30)
    domain = models.ForeignKey(DomainName)

# Create your models here.
