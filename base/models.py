
import os
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

def path_and_rename(instance, filename):
    upload_to = "Images/"
    ext = filename.split('.')[-1]
    # get filename
    if instance.user.username:
        filename = 'User_Profile_Pictures/{}.{}'.format(instance.user.username,ext)
    return os.path.join(upload_to,filename)

# student model to save the additional details of student in db
class Student(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    standard = models.CharField(max_length=100)
    grade = models.CharField(max_length=10)
    section = models.CharField(max_length=100)
    stream = models.CharField(max_length=100)
    roll_no = models.IntegerField()
    profile_pic = models.ImageField(upload_to = path_and_rename,verbose_name= 'Profile Picture',blank=True )
    is_staff = models.BooleanField(
        _("educator"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated','-created']
    
    def __str__(self):
        return self.user.username

# educator model to save the additional details of educator in db
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
    is_staff = models.BooleanField(
        _("educator"),
        default=True,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    

    class Meta:
        ordering = ['-updated','-created']
    
    def __str__(self):
        return self.user.username