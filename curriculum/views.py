from django.contrib.messages import constants as messages
from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth.decorators import login_required
def hello(request):
    return HttpResponse('hello world!!')

# get all the standards of the school
def StandardListView(request):

    if request.user.is_authenticated:
        page = 'after_login'
        user = request.user
        standards = Standard.objects.all()
        context = {
            'page':page,
            'user':user,
            'standards':standards
        }
        return render(request,'curriculum/standard_list_view.html',context)
    return HttpResponse("you are not logged in login first!!")

# get all the subjects in particular standard 
def SubjectListView(request,pk):
    if request.user.is_authenticated:
        page = 'after_login'
        user = request.user
        # get all the subjects in required standard
        standard = Standard.objects.filter(standard_id=pk).first()
        print("standard = ",standard)
        subjects = Subject.objects.filter(standard=standard)
        print("subjects = ",subjects)
        


        context = {
                'page':page,
                'user':user,
                'subjects':subjects,
            }
        return render(request,'curriculum/subject_list_view.html',context)
    return HttpResponse("you are not logged in login first!!")

# def LessonListView(request,pk):

