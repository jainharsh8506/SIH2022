from django.contrib import admin
from django.urls import path
from NWNS import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name="about"),
    path("university", views.university, name="university"),
    path("standalone", views.standalone, name="standalone"),
    path("college_institution", views.college_institution, name="college_institution")
    
]