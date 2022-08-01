
from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home,name = 'home'),
    # path('register/',views.registerPage,name = 'register'),
    path('register/',views.defaultRegister,name = 'register'),
    path('user/register/',views.userRegisterPage,name = 'user-register'),
    path('educator/register/',views.educatorRegisterPage,name = 'educator-register'),
    path('login/',views.loginPage,name = 'login'),
    path('logout/',views.logoutUser,name = 'logout'),
    path('profile/',views.profilePage,name = 'profile'),
]
