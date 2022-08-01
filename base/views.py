from operator import index
from urllib import response
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.db.models import Q
# from .forms import UserForm
from django.contrib.auth.forms import UserCreationForm 

def defaultRegister(request):
    page = 'before_login'

    context = {'page':page}
    return render(request,'base/defaultRegister.html',context)

def userRegisterPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    # user = request.user
    role = 'User'
    page = 'before_login'
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        print("message = this is a post request")
        print("form = ",form)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = False
            user.save()
            print("message = this is after valid form")
            
            print("form = ",form)
            login(request,user)
            print("user = ",user)
            print("EMAIL = ",user.email)
            return redirect('home')
        else:
            print("message = form is not being valid")
            print(messages.error)
            messages.error(request, 'An error occured during registration..')
            
    context  ={'form':form,'page':page,'role':role}
    return render(request,'base/registerPage.html',context)

def educatorRegisterPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    role = 'Educator'
    page = 'before_login'
    form = EducatorForm()
    if request.method == 'POST':
        form = EducatorForm(request.POST)
        print("form = ",form)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.save()

            print("user = ",request.user)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # user = authenticate(request,username=username,password=password)
            login(request,user)
            print("EMAIL = ",user.email)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during registration..')
            
    context  ={'form':form,'page':page,'role':role}
    return render(request,'base/registerPage.html',context)



def loginPage(request):
    page = 'before_login'
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password  = request.POST.get('password')
        # print(phone)
        print(password)
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'user does not exist...')
        user =  authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('home')

    context = {'page': page}
    return render(request,'base/loginPage.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def profilePage(request):
    page = 'after_login'
    user = request.user

    context = {'page':page,'user':user}
    return render(request,'base/profilePage.html',context)

@login_required(login_url='login')
def home(request):
    page = 'after_login'
    context = {'page':page}
    return render(request,'base/homePage.html',context)

