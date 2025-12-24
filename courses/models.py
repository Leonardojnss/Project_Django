from django.db import models

class Course(models.Model):
    LEVEL_CHOICE = (
        ('B', 'Basic'),
        ('I', 'Intermediate'),
        ('A', 'Advanced')
    )
    title = models.CharField(max_length=150)
    description = models.TextField()        
    duration = models.IntegerField()        
    price = models.DecimalField(max_digits=8, decimal_places=2)
    level = models.CharField(max_length=1, choices=LEVEL_CHOICE, default='B')

    def __str__(self):
        return self.title