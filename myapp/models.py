from django.db import models

# Create your models here.
class Student(models.Model):
   
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=200)
    rollno = models.IntegerField()
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    email = models.EmailField(max_length=200)
    mobile = models.IntegerField()
    guardian_mobile = models.IntegerField()
    


