import pandas as pd
from django.db import connection
from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse
from .models import CollegeInstitution, CollegeInstitutionAccreditation,Accreditation,Faculty, College, Infrastructure, StandaloneInstitution, UniversityAccreditation, University
from django.http import JsonResponse



# Create your views here.

def index(request):
    p=CollegeInstitution.objects.raw(' SELECT college_institution_accreditation.college_institution_id,college_institution.name,college_institution_accreditation.accreditation_id,college_institution_accreditation.survey_year,accreditation.accreditation_body,accreditation.score,accreditation.max_score,(accreditation.score/accreditation.max_score)*100 AS result FROM  college_institution_accreditation,accreditation WHERE (college_institution_accreditation.accreditation_id = accreditation.id) AND (college_institution_accreditation.id=college_institution.accreditation) ORDER BY result DESC') 
    context = {'p': p }
    return render(request,'index.html',context)

def index(request):
    q=CollegeInstitution.objects.raw(' SELECT college_institution.id, college_institution.name, course.discipline,examination_result.result, educational_institution_course.course_id FROM college_institution , course, educational_institution_course, examination_result WHERE (educational_institution_course.course_id= examination_result.course_id) AND (examination_result.course_id=course.id) AND (educational_institution_course.institution_id= college_institution.id) ORDER BY result DESC');
    {'q': q}
    return render(request,'index.html',context)
def index(request):
    r=University.objects.raw(' SELECT university_accreditation.university_id,university_accreditation.accreditation_id,university_accreditation.survey_year,accreditation.accreditation_body,accreditation.score,accreditation.max_score,(accreditation.score/accreditation.max_score)*100 AS result, FROM  university_accreditation,accreditation WHERE (university_accreditation.accreditation_id = accreditation.id) AND (_accreditation.id=college_institution.accreditation) ORDER BY result DESC') 
    context={'r':r} 
    return render(request,'index.html',context)
def index(request):
    s=university.objects.raw(' SELECT university.id, university.name, course.discipline,examination_result.result, educational_institution_course.course_id FROM university , course, educational_institution_course, examination_result WHERE (educational_institution_course.course_id= examination_result.course_id) AND (examination_result.course_id=course.id) AND (educational_institution_course.institution_id= university.id) ORDER BY result DESC');
    context{'s' : s }
    return render(request,'index.html',context)
#def index(request):
 # p = StandaloneInstitutionAccreditation.objects.raw(' SELECT Standalone_institution_accreditation.standalone_institution_id,standalone_institution_accreditation.accreditation_id,standalone_institution_accreditation.survey_year,accreditation.accreditation_body,accreditation.score,accreditation.max_score,accreditation.has_score FROM standalone_institution_accreditation,accreditation WHERE standalone_institution_accreditation.accreditation_id = accreditation.id') 
# q = StandaloneInstitution.objects.raw(' SELECT standalone_institution.id, standalone_institution.name, course.discipline, examination_result.result, educational_institution_course.course_id FROM standalone_institution , course, educational_institution_course, examination_result WHERE (educational_institution_course.course_id= examination_result.course_id) AND (examination_result.course_id=course.id) AND (educational_institution_course.institution_id= standalone_institution.id) ORDER BY result DESC')
    #context = {'p': p , 'q': q }
    #return render(request,'index.html',context)





#def index(request):
   # r=str(CollegeInstitution.objects.raw('SELECT college_institution.id,college_institution.name,college_institution.infrastructure_id FROM college_institution,infrastructure WHERE (college_institution.infrastructure_id=infrastructure.id) AND (infrastructure.laboratory=TRUE)AND (infrastructure.library=TRUE) AND (infrastructure.connectivity_nkn=TRUE) AND (infrastructure.computer_center=TRUE) AND (infrastructure.health_center=TRUE) AND (infrastructure.cafeteria=TRUE) AND (infrastructure.playground=TRUE) AND (infrastructure.indoor_stadium=TRUE) AND (infrastructure.gymnasium_fitness_center=TRUE) AND (infrastructure.guest_house=TRUE) AND (infrastructure.separate_room_for_girls=TRUE)'))
   # df= pd.read_sql_query(r,connection)
   # context={'r':r}
   # return render(request,'index.html',context)


#def index(request):
    #q=university.objects.raw('ELECT university.id,university.name,university.infrastructure_id FROM university,infrastructure WHERE (university.infrastructure_id=infrastructure.id) AND (infrastructure.laboratory=TRUE)AND (infrastructure.library=TRUE) AND (infrastructure.connectivity_nkn=TRUE) AND (infrastructure.computer_center=TRUE) AND (infrastructure.health_center=TRUE) AND (infrastructure.cafeteria=TRUE) AND (infrastructure.playground=TRUE) AND (infrastructure.indoor_stadium=TRUE) AND (infrastructure.gymnasium_fitness_center=TRUE) AND (infrastructure.guest_house=TRUE) AND (infrastructure.separate_room_for_girls=TRUE)');
    #context={'q':q}
    #return render(request,'index.html',context)

#def index(request):
    #r=StandaloneInstitution.objects.raw('SELECT standalone_institution.id,standalone_institution.name,standalone_institution.infrastructure_id FROM standalone_institution,infrastructure WHERE (standalone_institution.infrastructure_id=infrastructure.id) AND (infrastructure.laboratory=TRUE)AND (infrastructure.library=TRUE) AND (infrastructure.connectivity_nkn=TRUE) AND (infrastructure.computer_center=TRUE) AND (infrastructure.health_center=TRUE) AND (infrastructure.cafeteria=TRUE) AND (infrastructure.playground=TRUE) AND (infrastructure.indoor_stadium=TRUE) AND (infrastructure.gymnasium_fitness_center=TRUE) AND (infrastructure.guest_house=TRUE) AND (infrastructure.separate_room_for_girls=TRUE)');
    #context={'r':r}
    #return render(request,'index.html',context)

#def index(request):
    credentials = "postgresql://root:root@http://127.0.0.1:8000/:5432/data_user_2019"
    dataframe=pd.read.sql(CollegeInstitution.objects.raw('SELECT college_institution.id,college_institution.name,infrastructure.no_of_books,infrastructure.no_of_journals FROM college_institution,infrastructure WHERE (college_institution.infrastructure_id=infrastructure.id)'));
    context={'dataframe':dataframe}
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