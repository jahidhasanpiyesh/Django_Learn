from django.urls import path
from course import views
urlpatterns = [
    path('co/', views.coursefirst),
    path('cou/', views.coursesecond),
]
