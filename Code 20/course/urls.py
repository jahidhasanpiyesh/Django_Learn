from django.urls import path
from course import views
urlpatterns = [
    path('courseone/',views.courseone),
    path('coursetwo/',views.coursetwo),
]