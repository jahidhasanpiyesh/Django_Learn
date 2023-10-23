from django.urls import path
from filter_app import views
urlpatterns = [
    path('',views.filter_pro),
]