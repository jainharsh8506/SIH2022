from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse
from .models import InstituteTypeName, RefInstituteType , College, CollegeInstitution, StandaloneInstitution, University, CollegeInstitutionAccreditation,Accreditation,Faculty, Infrastructure
from django.http import JsonResponse
# Create your views here.

def index(request):
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
    context={'coll_name':college, 'college_name':college_name}    
    return render(request,'college_institution.html',context)


