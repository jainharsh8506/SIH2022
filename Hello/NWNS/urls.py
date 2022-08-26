from django.contrib import admin
from django.urls import path
from NWNS import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.index, name='home'),
    path("about.html", views.about, name="about"),
    path("contact.html", views.contact, name="contact"),
    path("courses.html", views.courses, name="courses"),
    path("index.html", views.index, name="index"),
    path("college_institution.html", views.college_institution, name="college_institution"),
    path("examination_result_college_institution.html", views.examination_result_college_institution, name="examination_result_college_institution"),
    path("infrastructure_college_institution.html", views.infrastructure_college_institution, name="infrastructure_college_institution"),
    path("choose_multiple_parameters_college_institution.html", views.choose_multiple_parameters_college_institution, name="choose_multiple_parameters_college_institution"),
    path("placement_college_institution.html", views.placement_college_institution, name="placement_college_institution"),
    path("sfr_college_institution.html", views.sfr_college_institution, name="sfr_college_institution"),
    path("accreditation_college_institution.html", views.accreditation_college_institution, name="accreditation_college_institution"),
    path("standalone_institution.html", views.standalone_institution, name="standalone_institution"),
    path("infrastructure_standalone_institution.html", views.infrastructure_standalone_institution, name="infrastructure_standalone_institution"),
    path("examination_result_standalone.html", views.examination_result_standalone_institution, name="examination_result_standalone"),
    path("choose_multiple_parameters_standalone_institution.html", views.choose_multiple_parameters_standalone_institution, name="choose_multiple_parameters_standalone_institution"),
    path("placement_standalone_institution.html", views.placement_standalone_institution, name="placement_standalone_institution"),
    path("sfr_standalone_institution.html", views.sfr_standalone_institution, name="sfr_standalone_institution"),
    path("accreditation_standalone_institution.html", views.accreditation_standalone_institution, name="accreditation_standalone_institution"),
    path("university.html", views.university, name="university"),
    path("infrastructure_university.html", views.infrastructure_university, name="infrastructure_university"),
    path("examination_result_university.html", views.examination_result_university, name="examination_result_university"),
    path("choose_multiple_parameters_university.html", views.choose_multiple_parameters_university, name="choose_multiple_parameters_university"),
    path("placement_university.html", views.placement_university, name="placement_university"),
    path("sfr_university.html", views.sfr_university, name="sfr_university"),
    path("accreditation_university.html", views.accreditation_university, name="accreditation_university"),
    path("start.html", views.start, name="start"),
    path("test.html", views.test, name="test"),
    path("accreditation_infrastructure", views.accreditation_infrastructure, name="table")
]
urlpatterns+= staticfiles_urlpatterns()