

from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.validators import RegexValidator
from .manager import UserManager

class User(AbstractBaseUser):
    email = models.EmailField(
        max_length=255,
        unique=True,
        null=True,
    )
    username = models.CharField(max_length=50, default="")
    phone_regex = RegexValidator(regex=r'^([0|+[0-9]{1,5})?([7-9][0-9]{9})$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.")
    phone = models.CharField(validators=[
        phone_regex], max_length=10, unique=True, null=True)  # validators should be a list
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    # fields for registeration user + educator
    # --> user form fields
    standard = models.CharField(max_length=10,null=True,default='null')
    grade = models.CharField(max_length=10,null=True,default='null')
    section = models.CharField(max_length=20,default='null')
    stream = models.CharField(max_length=50,default='null')
    roll_no = models.IntegerField(default=-1)
    # --> educator form fields
    subject = models.CharField(max_length=100,default='null')
    classes_taught = models.CharField(max_length=100,default='null')


    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return str(self.email)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def save(self, *args, **kwargs) -> None:
        return super().save(*args, **kwargs)

class Message(models.Model):
    educator = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created','-updated']
    
    def __str__(self):
        return str(self.body[0:50])

class UserRegisterModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    email = models.EmailField()
    standard = models.CharField(max_length=10)
    grade = models.CharField(max_length=10)
    section = models.CharField(max_length=20)
    stream = models.CharField(max_length=50)
    roll_no = models.IntegerField()

    def __str__(self):
        return str(self.user.username)


# class Student(models.Model):
#     id = models.AutoField(primary_key=True)
#     # user = models.ForeignKey(User,on_delete=models.CASCADE)
#     name = models.ForeignKey(User,on_delete=models.CASCADE)
#     standard = models.CharField(max_length=10)
#     grade = models.CharField(max_length=10)
#     section = models.CharField(max_length=10)
#     stream = models.CharField(max_length=100)
#     roll_no = models.IntegerField()
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         # model = User
#         ordering = ['-updated','-created']
    
#     def __str__(self):
#         return str(self.name)

# class Educator(models.Model):
#     id = models.AutoField(primary_key=True)
#     # user = models.ForeignKey(User,on_delete=models.CASCADE)
#     educator = models.ForeignKey(User,on_delete=models.CASCADE)
#     subject = models.CharField(max_length=50)
#     classes_taught = models.CharField(max_length=50)
#     contact_no = models.IntegerField()
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)
    

#     class Meta:
#         # model = User
#         ordering = ['-updated','-created']
    
#     def __str__(self):
#         return str(self.educator)