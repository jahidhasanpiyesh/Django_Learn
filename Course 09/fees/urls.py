from django.urls import path
from fees import views
urlpatterns = [
    path('fe/', views.feesfirst),
    path('fee/', views.feessecond),
]
