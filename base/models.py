

from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    standard = models.CharField(max_length=100)
    grade = models.CharField(max_length=10)
    section = models.CharField(max_length=100)
    stream = models.CharField(max_length=100)
    roll_no = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated','-created']
    
    def __str__(self):
        return self.user.username

class Educator(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^([0|+[0-9]{1,5})?([7-9][0-9]{9})$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.")
    phone = models.CharField(validators=[
        phone_regex], max_length=10, unique=True,null=True)
    subject = models.CharField(max_length=50)
    classes_taught = models.CharField(max_length=50)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ['-updated','-created']
    
    def __str__(self):
        return self.user.username