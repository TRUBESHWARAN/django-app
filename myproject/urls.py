"""
URL configuration for myproject project.

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
from app1.views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homePage,name='main'),
    path('about/',aboutPage,name='ab'),
    path('courses/',coursePage,name='cr'),
    path('enquirenow/',enquiryPage, name='enq'),
    path('enquiries/',enquiries,name='enqs'),
    path('enquiries/edit/<id>/',editPage,name='edit'),
    path('enquiries/delete/<id>/',deletePage,name='del'),
    path('addStudent/',login_required(AddStudent.as_view()),name='adds'),
    path('viewstudents/',login_required(ViewStudents.as_view()),name='views'),
    path('viewstudents/edit/<id>/',login_required(UpdateStudent.as_view()),name='update'),
    path('viewstudents/delete/<id>/',login_required(DeleteStudent.as_view()),name='dels'),
    path('staffpage/',profilePage,name='profile'),
    path('signup/',signup,name='sign'),
    path('login/',LoginView.as_view(template_name = 'login.html'),name='login'),
    path('logout/',LogoutView.as_view(next_page='/'),name='logout'),

    path('password_reset/',PasswordResetView.as_view(template_name='password1.html'),name='password_reset'),
    path('password_reset_done/',PasswordResetDoneView.as_view(template_name='password2.html'),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='password3.html'),name='password_reset_confirm'),
    path('password_reset_complete/',PasswordResetCompleteView.as_view(template_name='password4.html'),name='password_reset_complete'),
]
