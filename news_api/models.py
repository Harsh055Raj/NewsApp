from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

    
    
# class Newsletter(models.Model):
#     email=models.EmailField(max_length = 100)
    

from django.utils import timezone


class Subscribers(models.Model):
    email = models.EmailField(null=True)

    def __str__(self):
        return self.email


class MailMessage(models.Model):
    title = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=158)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name