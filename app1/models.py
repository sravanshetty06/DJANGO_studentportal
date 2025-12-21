from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    email=models.EmailField(max_length=25)
    dob=models.DateField(max_length=20)
    cell=models.BigIntegerField()