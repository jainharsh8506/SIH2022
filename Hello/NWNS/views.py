import pandas as pd
from django.db import connection
from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse
from .models import CollegeInstitution, CollegeInstitutionAccreditation,Accreditation,Faculty, College, Infrastructure, StandaloneInstitution, UniversityAccreditation, University ,StandaloneInstitutionAccreditation
from django.http import JsonResponse



# Create your views here.

def index(request):
    college_institution_accreditation=CollegeInstitution.objects.raw(' SELECT college_institution_accreditation.college_institution_id,college_institution.name,college_institution_accreditation.accreditation_id,college_institution_accreditation.survey_year,accreditation.accreditation_body,accreditation.score,accreditation.max_score,(accreditation.score/accreditation.max_score)*100 AS result FROM  college_institution_accreditation,accreditation WHERE (college_institution_accreditation.accreditation_id = accreditation.id) AND (college_institution_accreditation.id=college_institution.accreditation) ORDER BY result DESC') 
    context = {'college_institution_accreditation': college_institution_accreditation }
    return render(request,'index.html',context)

def index(request):
    college_institution_result=CollegeInstitution.objects.raw(' SELECT college_institution.id, college_institution.name, course.discipline,examination_result.result, educational_institution_course.course_id FROM college_institution , course, educational_institution_course, examination_result WHERE (educational_institution_course.course_id= examination_result.course_id) AND (examination_result.course_id=course.id) AND (educational_institution_course.institution_id= college_institution.id) ORDER BY result DESC');
    context={'college_institution_resul': college_institution_result}
    return render(request,'index.html',context)

def index(request):
    university_accreditation=University.objects.raw(' SELECT university_accreditation.university_id,university_accreditation.accreditation_id,university_accreditation.survey_year,accreditation.accreditation_body,accreditation.score,accreditation.max_score,(accreditation.score/accreditation.max_score)*100 AS result, FROM  university_accreditation,accreditation WHERE (university_accreditation.accreditation_id = accreditation.id) AND (_accreditation.id=college_institution.accreditation) ORDER BY result DESC') 
    context={'university_accreditation':university_accreditation }
    return render(request,'index.html',context)

def index(request):
  standalone_institution_accreditation = StandaloneInstitution.objects.raw(' SELECT Standalone_institution_accreditation.standalone_institution_id,standalone_institution_accreditation.accreditation_id,standalone_institution_accreditation.survey_year,accreditation.accreditation_body,accreditation.score,accreditation.max_score,(accreditation.score/accreditation.max_score)*100 AS result FROM standalone_institution_accreditation,accreditation WHERE standalone_institution_accreditation.accreditation_id = accreditation.id') 
  context = {'standalone_institution_accreditation ': standalone_institution_accreditation }
  return render(request,'index.html',context)

def index(request):
    standalone_institution_result = StandaloneInstitution.objects.raw(' SELECT standalone_institution.id, standalone_institution.name, course.discipline, examination_result.result, educational_institution_course.course_id FROM standalone_institution , course, educational_institution_course, examination_result WHERE (educational_institution_course.course_id= examination_result.course_id) AND (examination_result.course_id=course.id) AND (educational_institution_course.institution_id= standalone_institution.id) ORDER BY result DESC')
    context = { 'standalone_institution_result': standalone_institution_result }
    return render(request,'index.html',context)

def index(request):
    university_result=university.objects.raw(' SELECT university.id, university.name, course.discipline,examination_result.result, educational_institution_course.course_id FROM university , course, educational_institution_course, examination_result WHERE (educational_institution_course.course_id= examination_result.course_id) AND (examination_result.course_id=course.id) AND (educational_institution_course.institution_id= university.id) ORDER BY result DESC');
    context={'university_result' : university_result }
    return render(request,'index.html',context)

def index(request):
   college_institution_infrastucture=CollegeInstitution.objects.raw('SELECT college_institution.id,college_institution.name,college_institution.infrastructure_id FROM college_institution,infrastructure WHERE (college_institution.infrastructure_id=infrastructure.id) AND (infrastructure.laboratory=TRUE)AND (infrastructure.library=TRUE) AND (infrastructure.connectivity_nkn=TRUE) AND (infrastructure.computer_center=TRUE) AND (infrastructure.health_center=TRUE) AND (infrastructure.cafeteria=TRUE) AND (infrastructure.playground=TRUE) AND (infrastructure.indoor_stadium=TRUE) AND (infrastructure.gymnasium_fitness_center=TRUE) AND (infrastructure.guest_house=TRUE) AND (infrastructure.separate_room_for_girls=TRUE)'))
   context={'college_institution_infrastucture':college_institution_infrastucture}
   return render(request,'index.html',context)


def index(request):
    university_infrastructure=university.objects.raw('SELECT university.id,university.name,university.infrastructure_id FROM university,infrastructure WHERE (university.infrastructure_id=infrastructure.id) AND (infrastructure.laboratory=TRUE)AND (infrastructure.library=TRUE) AND (infrastructure.connectivity_nkn=TRUE) AND (infrastructure.computer_center=TRUE) AND (infrastructure.health_center=TRUE) AND (infrastructure.cafeteria=TRUE) AND (infrastructure.playground=TRUE) AND (infrastructure.indoor_stadium=TRUE) AND (infrastructure.gymnasium_fitness_center=TRUE) AND (infrastructure.guest_house=TRUE) AND (infrastructure.separate_room_for_girls=TRUE)');
    context={'university_infrastructure':university_infrastructure}
    return render(request,'index.html',context)

def index(request):
    standalone_institution_infrastructure=StandaloneInstitution.objects.raw('SELECT standalone_institution.id,standalone_institution.name,standalone_institution.infrastructure_id FROM standalone_institution,infrastructure WHERE (standalone_institution.infrastructure_id=infrastructure.id) AND (infrastructure.laboratory=TRUE)AND (infrastructure.library=TRUE) AND (infrastructure.connectivity_nkn=TRUE) AND (infrastructure.computer_center=TRUE) AND (infrastructure.health_center=TRUE) AND (infrastructure.cafeteria=TRUE) AND (infrastructure.playground=TRUE) AND (infrastructure.indoor_stadium=TRUE) AND (infrastructure.gymnasium_fitness_center=TRUE) AND (infrastructure.guest_house=TRUE) AND (infrastructure.separate_room_for_girls=TRUE)');
    context={'standalone_institution_infrastructure':standalone_institution_infrastructure}
    return render(request,'index.html',context)

def index(request):
    college_institution_journals=CollegeInstitution.objects.raw('SELECT college_institution.id,college_institution.name,infrastructure.no_of_journals FROM college_institution,infrastructure WHERE (college_institution.infrastructure_id=infrastructure.id) ORDER BY infrastructure.no_of_journals DESC'));
    context={'college_institution_journals':college_institution_journals}
    return render(request,'index.html',context)

def index(request):
    standalone_institution_journals=StandaloneInstitution.objects.raw('SELECT standalone_institution.id,standalone_institution.name,infrastructure.no_of_journals FROM standalone_institution,infrastructure WHERE (standalone_institution.infrastructure_id=infrastructure.id) ORDER BY infrastructure.no_of_journals DESC'));
    context={'standalone_institution_journals':standalone_institution_journals}
    return render(request,'index.html',context)

def index(request):
    university_journals=CollegeInstitution.objects.raw('SELECT university.id,university.name,infrastructure.no_of_journals FROM standalone_institution,infrastructure WHERE (university.infrastructure_id=infrastructure.id) ORDER BY infrastructure.no_of_journals DESC'));
    context={'university_journals':university_journals}
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def university(request):
    return render(request,'university.html')

def standalone(request):
    return render(request,'standalone.html')

def college_institution(request):
    return render(request,'college_institution.html')



print(index)