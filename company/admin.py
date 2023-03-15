from django.contrib import admin
from .models import SchoolBoard, Contact, User
from django.contrib.auth.admin import UserAdmin

admin.site.register(SchoolBoard)
admin.site.register(Contact)
admin.site.register(User, UserAdmin)