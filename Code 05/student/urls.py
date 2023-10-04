"""
URL configuration for student project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# first way code show this output >>>
from course1 import views as c1
from course2 import views as c2

# second way code show this output >>>
from course1.views import cour11
from course2.views import cour22
urlpatterns = [
    path('admin/', admin.site.urls),
    # First way
    path('course1/', c1.cour1),
    path('course2/', c2.cour2),

    # Second way
    path('course11/', cour11),
    path('course22/', cour22),
]
