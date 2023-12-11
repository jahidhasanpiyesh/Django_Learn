from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.course),
    path('success/',views.massage),
]
