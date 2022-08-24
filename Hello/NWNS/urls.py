from django.contrib import admin
from django.urls import path
from NWNS import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.index, name='home'),
    path("about.html", views.about, name="about"),
    path("contact.html", views.contact, name="contact"),
    path("courses.html", views.standalone, name="courses"),
    path("index.html", views.index, name="index"),
    path("accreditation_infrastructure", views.accreditation_infrastructure, name="table")
]
urlpatterns+= staticfiles_urlpatterns()