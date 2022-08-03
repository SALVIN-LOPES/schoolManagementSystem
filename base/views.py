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

# routing to default register page
def defaultRegister(request):
    page = 'before_login'

    context = {'page':page}
    return render(request,'base/defaultRegister.html',context)

# routing to userRegisterPage
def userRegisterPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    # user = request.user
    role = 'User'
    page = 'before_login'
    user_form = UserForm()
    student_form = StudentForm()

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        student_form = StudentForm(data=request.POST)

        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save(commit=False)
            user.is_staff = False
            user.save()

            stu_form = student_form.save(commit=False)
            stu_form.user = user
            stu_form.save()

            login(request,user)
            return redirect('home')
        else:
            print("message = form is not being valid")
            print(messages.error)
            messages.error(request, 'An error occured during registration..')
            
    context  ={'user_form':user_form,'student_form':student_form,'page':page,'role':role}
    return render(request,'base/UserRegisterPage.html',context)

#routing to educatorRegisterPage
def educatorRegisterPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    role = 'Educator'
    page = 'before_login'
    user_form = UserForm()
    educator_form = EducatorForm()

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        educator_form = EducatorForm(data=request.POST)

        if user_form.is_valid() and educator_form.is_valid():
            user = user_form.save(commit=False)
            user.is_staff = True
            user.save()

            edu_form = educator_form.save()
            edu_form.user = user
            edu_form.save()
            # user = authenticate(request,username=username,password=password)
            login(request,user)
            print("EMAIL = ",user.email)
            return redirect('home')
        else:
            print("form not valid")
            messages.error(request, 'An error occured during registration..')
            
    context  ={'user_form':user_form,'educator_form':educator_form,'page':page,'role':role}
    return render(request,'base/EducatorRegisterPage.html',context)


# creating logion page and saving the user
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

# creating logout logic
def logoutUser(request):
    logout(request)
    return redirect('login')

# to access profile page user needs to login first and redirecting to profile page
@login_required(login_url='login')
def profilePage(request):
    page = 'after_login'
    user = request.user
    print('status = ', user.is_staff)
    print("user = ",user.username)
    if not user.is_staff:
        student = Student.objects.filter(user=user).first()
        print("student = ",student)
        context = {'page':page,'user':user,'student':student}
        return render(request,'base/profilePage.html',context)
    else:
        educator = Educator.objects.filter(user=user).first()
        print("educator = ",educator)
        context = {'page':page,'user':user,'educator':educator}
        return render(request,'base/profilePage.html',context)

# to access home page user needs to login first and redirecting to home page
@login_required(login_url='login')
def home(request):
    page = 'after_login'
    context = {'page':page}
    return render(request,'base/homePage.html',context)

