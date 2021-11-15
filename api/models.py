from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    number_of_pages = models.PositiveIntegerField()
    publisher = models.CharField(max_length=200)
    release_date = models.DateField()

    def __str__(self):
        return self.name
