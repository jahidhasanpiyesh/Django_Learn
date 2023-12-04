from django.contrib import admin
from course.models import Student
# Register your models here.

# First Way show this all data views--------
# class StudentAdmin(admin.ModelAdmin):
#     # just use list or tuple type value :
#     list_display=["id","stuname","stuemail","stupass"]

# admin.site.register(Student,StudentAdmin)


# Second way Show this all data views -------
# its very essy ------way fix this probelm -----
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # just use list or tuple type value :
    list_display=["id","stuname","stuemail","stupass"]