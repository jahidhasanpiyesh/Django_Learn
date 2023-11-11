from django.urls import path
from fees import views
urlpatterns = [
    path('feesone/',views.feesone),
    path('feestwo/',views.feestwo),
]