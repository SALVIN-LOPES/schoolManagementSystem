from django import forms
from django.contrib.auth.forms import UserCreationForm  
# from django.contrib.auth.models import User
from .models import *

class UserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta():
        model = User
        fields = ('username','email','password1','password2')
        labels = {
            'password1':'Password',
            'password2':'confirm Password'
        }

class StudentForm(forms.ModelForm):
    standard = forms.CharField(max_length=10)
    grade = forms.CharField(max_length=10)
    section = forms.CharField(max_length=20)
    stream = forms.CharField(max_length=50)
    roll_no = forms.IntegerField()

    class Meta:
        model = Student
        fields = ('standard','grade',
        'section','stream','roll_no',
        
        )

class EducatorForm(forms.ModelForm):
    subject = forms.CharField(max_length=100)
    classes_taught = forms.CharField(max_length=100)

    class Meta:
        model = Educator
        fields = ('subject','classes_taught',
        'phone'
        
        )


