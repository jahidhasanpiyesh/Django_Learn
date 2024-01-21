from django.contrib import admin
from .models import User
# Register your models here.

@admin.register(User)
class adminregister(admin.ModelAdmin):
    list_display = ('studentname','techername','email','password')