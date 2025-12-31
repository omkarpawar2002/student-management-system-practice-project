from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255,null=False)
    last_name = models.CharField(max_length=255,null=False)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    mobile_number = models.CharField(max_length=15)
    city = models.CharField(max_length=255,null=False)
    address = models.TextField(max_length=255,null=False)
    subject = models.CharField(max_length=50,null=False)
    subject_image = models.ImageField(upload_to='./Images/')
    email = models.EmailField(max_length=255,unique=True,null=False)
    password = models.CharField(max_length=100)
    eligible = models.BooleanField()

