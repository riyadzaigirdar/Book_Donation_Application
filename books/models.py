from django.db import models
from datetime import datetime


class Category(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category


class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_publised = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
