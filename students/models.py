from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    cpf = models.CharField(max_length=11, unique=True)  # prevent duplicate CPF
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=14)

    def __str__(self):
        return self.name
    