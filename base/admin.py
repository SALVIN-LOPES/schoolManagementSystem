from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from .forms import *

admin.site.register(Student)
admin.site.register(Educator)