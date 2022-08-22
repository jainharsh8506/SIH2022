import pandas as pd
from django.db import connection
from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse
from .models import CollegeInstitution, CollegeInstitutionAccreditation, RefInstituteType, StandaloneInstitution, University
from django.http import JsonResponse

# Create your views here.

def index(request):
    college_institution_accreditation=CollegeInstitution.objects.raw(' SELECT college_institution_accreditation.college_institution_id,college_institution.name,college_institution_accreditation.accreditation_id,college_institution_accreditation.survey_year,accreditation.accreditation_body,accreditation.score,accreditation.max_score,(accreditation.score/accreditation.max_score)*100 AS result FROM  college_institution_accreditation,accreditation WHERE (college_institution_accreditation.accreditation_id = accreditation.id) AND (college_institution_accreditation.id=college_institution.accreditation) ORDER BY result DESC') 
    context = {'college_institution_accreditation': college_institution_accreditation }

    college=CollegeInstitution.objects.all()
    university=University.objects.all()
    standalone=StandaloneInstitution.objects.all()
    institute_type=RefInstituteType.objects.all()
    insti_type= request.GET.get('inst_type')
    college_name= request.GET.get('college_name')
    standalone_name=request.GET.get('standalone_name')
    university_name=request.GET.get('university_name')
    q=CollegeInstitution.objects.raw(' SELECT college_institution.id, college_institution.name, course.discipline,(examination_result.passed_total/NULLIF(examination_result.appeared_total,0))*100 AS result, educational_institution_course.course_id FROM college_institution , course, educational_institution_course, examination_result WHERE (educational_institution_course.course_id= examination_result.course_id) AND (examination_result.course_id=course.id) AND (educational_institution_course.institution_id= college_institution.id) ORDER BY result DESC');
    context={'standalone_name':standalone_name ,'university_name':university_name, 'q':q,'coll_name':college, 'Type':institute_type, 'ins_type':insti_type, 'univ_name':university, 'stand_name':standalone, 'college_name':college_name}    
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
    college_institution_infrastucture=CollegeInstitution.objects.raw('SELECT college_institution.id,college_institution.name,college_institution.infrastructure_id FROM college_institution,infrastructure WHERE (college_institution.infrastructure_id=infrastructure.id) AND (infrastructure.laboratory=TRUE)AND (infrastructure.library=TRUE) AND (infrastructure.connectivity_nkn=TRUE) AND (infrastructure.computer_center=TRUE) AND (infrastructure.health_center=TRUE) AND (infrastructure.cafeteria=TRUE) AND (infrastructure.playground=TRUE) AND (infrastructure.indoor_stadium=TRUE) AND (infrastructure.gymnasium_fitness_center=TRUE) AND (infrastructure.guest_house=TRUE) AND (infrastructure.separate_room_for_girls=TRUE)')
    context={'college_institution_infrastucture':college_institution_infrastucture}
    return render(request,'index.html',context)


def index(request):
    university_infrastructure=university.objects.raw('SELECT university.id,university.name,university.infrastructure_id FROM university,infrastructure WHERE (university.infrastructure_id=infrastructure.id) AND (infrastructure.laboratory=TRUE)AND (infrastructure.library=TRUE) AND (infrastructure.connectivity_nkn=TRUE) AND (infrastructure.computer_center=TRUE) AND (infrastructure.health_center=TRUE) AND (infrastructure.cafeteria=TRUE) AND (infrastructure.playground=TRUE) AND (infrastructure.indoor_stadium=TRUE) AND (infrastructure.gymnasium_fitness_center=TRUE) AND (infrastructure.guest_house=TRUE) AND (infrastructure.separate_room_for_girls=TRUE)')
    context={'university_infrastructure':university_infrastructure}
    return render(request,'index.html',context)

def index(request):
    standalone_institution_infrastructure=StandaloneInstitution.objects.raw('SELECT standalone_institution.id,standalone_institution.name,standalone_institution.infrastructure_id FROM standalone_institution,infrastructure WHERE (standalone_institution.infrastructure_id=infrastructure.id) AND (infrastructure.laboratory=TRUE)AND (infrastructure.library=TRUE) AND (infrastructure.connectivity_nkn=TRUE) AND (infrastructure.computer_center=TRUE) AND (infrastructure.health_center=TRUE) AND (infrastructure.cafeteria=TRUE) AND (infrastructure.playground=TRUE) AND (infrastructure.indoor_stadium=TRUE) AND (infrastructure.gymnasium_fitness_center=TRUE) AND (infrastructure.guest_house=TRUE) AND (infrastructure.separate_room_for_girls=TRUE)');
    context={'standalone_institution_infrastructure':standalone_institution_infrastructure}
    return render(request,'index.html',context)

def index(request):
    college_institution_journals=CollegeInstitution.objects.raw('SELECT college_institution.id,college_institution.name,infrastructure.no_of_journals FROM college_institution,infrastructure WHERE (college_institution.infrastructure_id=infrastructure.id) ORDER BY infrastructure.no_of_journals DESC')
    context={'college_institution_journals':college_institution_journals}
    return render(request,'index.html',context)

def index(request):
    standalone_institution_journals=StandaloneInstitution.objects.raw('SELECT standalone_institution.id,standalone_institution.name,infrastructure.no_of_journals FROM standalone_institution,infrastructure WHERE (standalone_institution.infrastructure_id=infrastructure.id) ORDER BY infrastructure.no_of_journals DESC')
    context={'standalone_institution_journals':standalone_institution_journals}
    return render(request,'index.html',context)

def index(request):
    university_journals=CollegeInstitution.objects.raw('SELECT university.id,university.name,infrastructure.no_of_journals FROM standalone_institution,infrastructure WHERE (university.infrastructure_id=infrastructure.id) ORDER BY infrastructure.no_of_journals DESC')
    context={'university_journals':university_journals}
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def university(request):
    university=University.objects.all()
    university_name=request.GET.get('university_name')
    context={'university_name':university_name, 'univ_name':university}    
    return render(request,'university.html',context)

def standalone(request):
    standalone=StandaloneInstitution.objects.all()
    standalone_name=request.GET.get('standalone_name')
    context={'standalone_name':standalone_name,'stand_name':standalone}    
    return render(request,'standalone.html',context)

def college_institution(request):
    college=CollegeInstitution.objects.all()
    college_name= request.GET.get('college_name')
    college_institution_result=CollegeInstitution.objects.raw(' SELECT college_institution.id, college_institution.name, course.discipline,examination_result.result, educational_institution_course.course_id FROM college_institution , course, educational_institution_course, examination_result WHERE (educational_institution_course.course_id= examination_result.course_id) AND (examination_result.course_id=course.id) AND (educational_institution_course.institution_id= college_institution.id) ORDER BY result DESC');
    college_exam1=request.GET.get('college_exam')
    context={'college_exam':college_exam1, 'coll_name':college, 'college_name':college_name, 'college_institution_result': college_institution_result}    
    return render(request,'college_institution.html',context)
