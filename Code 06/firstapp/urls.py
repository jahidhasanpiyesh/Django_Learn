from django.urls import path
from firstapp import views

urlpatterns = [
    path('first/' , views.firstapp),
    path('firstt/' , views.firstapps),
]