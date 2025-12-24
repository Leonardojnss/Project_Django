from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    isbn = models.CharField(max_length=13, unique=True)
    pages = models.IntegerField()
    available = models.BooleanField(default=True)
    published_date = models.DateField()


    def __str__(self):
        return self.title