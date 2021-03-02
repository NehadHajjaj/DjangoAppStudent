"""
Definition of urls for DjangoWebProject.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('student/', views.studentProfile, name='student'),
    path('teacher/', views.teacherProfile, name='teacher'),
    path('recommendation/', views.recommendationPage, name='recommendation'),
    path('<id>/editStudent/', views.editStudent, name='editStudent'),
    path('<id>/editTeacher/', views.editTeacher, name='editTeacher'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]
