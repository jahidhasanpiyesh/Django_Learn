from django.urls import path
from teg_app import views
urlpatterns = [
    path('',views.index),
]