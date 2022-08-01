from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from .forms import *

admin.site.register(Message)
# admin.site.register(Student)
# admin.site.register(Educator)
# class UserFormAdmin(UserAdmin):
#     add_form = UserForm
#     prepopulated_fields = {'username','email','standard','grade',
#         'section','stream','roll_no',}

# # admin.site.unregister(User)
# admin.site.register(User, UserAdmin)