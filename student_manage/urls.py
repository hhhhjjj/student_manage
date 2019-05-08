"""student_manage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from student_system.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_courses.html', get_courses),
    path('edit_courses.html', edit_courses),
    path('add_courses.html', add_courses),
    path('delete_courses.html', delete_courses),
    path('get_teacher.html', get_teacher),
    path('edit_teacher.html', edit_teacher),
    path('add_teacher.html', add_teacher),
    path('delete_teacher.html', delete_teacher),
    path('get_student.html', get_student),
    path('edit_student.html', edit_student),
    path('add_student.html', add_student),
    path('delete_student.html', delete_student),
    path('set_student.html', set_student),
    path('', home),
]
