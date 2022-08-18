from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse
from .models import CollegeInstitution, CollegeInstitutionAccreditation,Accreditation,Faculty, College, Infrastructure
from django.http import JsonResponse

# Create your views here.

def index(request):
   # p=CollegeInstitutionAccreditation.objects.raw(' SELECT college_institution_accreditation.college_institution_id,college_institution_accreditation.accreditation_id,college_institution_accreditation.survey_year,accreditation.accreditation_body,accreditation.score,accreditation.max_score,accreditation.has_score FROM  college_institution_accreditation,accreditation WHERE college_institution_accreditation.accreditation_id = accreditation.id') 
    q=CollegeInstitution.objects.raw(' SELECT college_institution.id, college_institution.name, course.discipline,(examination_result.passed_total/NULLIF(examination_result.appeared_total,0))*100 AS result, educational_institution_course.course_id FROM college_institution , course, educational_institution_course, examination_result WHERE (educational_institution_course.course_id= examination_result.course_id) AND (examination_result.course_id=course.id) AND (educational_institution_course.institution_id= college_institution.id) ORDER BY result DESC');
    #r=Infrastructure.objects.raw('UPDATE TABLE SET playground , library = CAST('TRUE' as bit)');
    context={'q':q }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def university(request):
    return render(request,'university.html')

def standalone(request):
    return render(request,'standalone.html')

def college_institution(request):
    return render(request,'college_institution.html')


