from django.db import models

class Card(models.Model):
    name = models.CharField(max_length=200)
    status = models.SlugField(max_length=200, unique=True)
    content = models.TextField(blank = True, null = True)
    category = models.CharField(max_length=200)
    author = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']