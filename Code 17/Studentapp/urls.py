from django.urls import path
from Studentapp import views
urlpatterns = [
    path('',views.student),
]
