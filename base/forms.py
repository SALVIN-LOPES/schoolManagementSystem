from django import forms
from django.contrib.auth.forms import UserCreationForm  
# from django.contrib.auth.models import User
from .models import *


class UserForm(UserCreationForm):
    email = forms.EmailField()
    standard = forms.CharField(max_length=10)
    grade = forms.CharField(max_length=10)
    section = forms.CharField(max_length=20)
    stream = forms.CharField(max_length=50)
    roll_no = forms.IntegerField()

    class Meta:
        model = User
        fields = ('username','email','standard','grade',
        'section','stream','roll_no','password1','password2'
        
        )
    # def save(self, commit=True):
    #     if not commit:
    #         raise NotImplementedError("Can't create User and UserProfile without database save")
    #     user = super(UserForm, self).save(commit=True)
    #     user_profile = UserRegisterModel(user=user, 
    #         email=self.cleaned_data['email'], 
    #         standard=self.cleaned_data['standard'],
    #         grade=self.cleaned_data['grade'],
    #         section=self.cleaned_data['section'],
    #         stream=self.cleaned_data['stream'],
    #         roll_no=self.cleaned_data['roll_no'],
    #         )
    #     user_profile.save()
    #     return user, user_profile

class EducatorForm(UserCreationForm):
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    classes_taught = forms.CharField(max_length=100)
    # contact_no = forms.IntegerField()

    class Meta:
        model = User
        fields = ('username','email','subject','classes_taught',
        'phone','password1','password2',
        
        )


