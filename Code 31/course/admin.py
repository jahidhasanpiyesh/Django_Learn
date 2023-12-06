from django.contrib import admin
from course.models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ["id","stuname","stuemail","stupass"]

admin.site.register(Student,StudentAdmin)