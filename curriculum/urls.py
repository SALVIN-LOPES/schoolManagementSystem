from django.contrib import admin
from django.urls import path, include
from . import views

app_name='curriculum'
urlpatterns = [
    path('', views.StandardListView,name='standard_list' ),
    path('<str:pk>/', views.SubjectListView,name='subject_list' ), #id = standard_id
    # path('<str:pk>/', views.LessonListView,name='lesson_list' ), #1stid = subject_id,#2ndid:lessons_list
]