from django.db import models

# Create your models here.
class TodolistItem(models.Model):
    content = models.TextField()
    
