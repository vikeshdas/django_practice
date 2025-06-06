from django.db import models
from django.urls import reverse



# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('basic_app:detail', kwargs={'pk':self.pk}) # pk stands for Primary Key

class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School,related_name='students',on_delete=models.CASCADE) # The related_name param will allow us to call this later on

    def __str__(self):
        return self.name
