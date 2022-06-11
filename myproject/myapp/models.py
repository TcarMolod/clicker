from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=1337)

class Fruits(models.Model):
    title = models.CharField(max_length=15)
    text = models.TextField(max_length=200)
    price = models.IntegerField()