from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse
from .models import InstituteTypeName, RefInstituteType , College, CollegeInstitution, StandaloneInstitution, University, CollegeInstitutionAccreditation,Accreditation,Faculty, Infrastructure
from django.http import JsonResponse
# Create your views here.

def index(request):
    college=CollegeInstitution.objects.all()
    university=University.objects.all()
    standalone=StandaloneInstitution.objects.all()
    #institute_type_name=InstituteTypeName.objects.all()
    institute_type=RefInstituteType.objects.all()
    insti_type= request.GET.get('inst_type')
    #inst_name= request.GET['inst_name']
    # p=CollegeInstitutionAccreditation.objects.raw(' SELECT college_institution_accreditation.college_institution_id,college_institution_accreditation.accreditation_id,college_institution_accreditation.survey_year,accreditation.accreditation_body,accreditation.score,accreditation.max_score,accreditation.has_score FROM  college_institution_accreditation,accreditation WHERE college_institution_accreditation.accreditation_id = accreditation.id') 
    q=CollegeInstitution.objects.raw(' SELECT college_institution.id, college_institution.name, course.discipline,(examination_result.passed_total/NULLIF(examination_result.appeared_total,0))*100 AS result, educational_institution_course.course_id FROM college_institution , course, educational_institution_course, examination_result WHERE (educational_institution_course.course_id= examination_result.course_id) AND (examination_result.course_id=course.id) AND (educational_institution_course.institution_id= college_institution.id) ORDER BY result DESC');
    #r=Infrastructure.objects.raw('UPDATE TABLE SET playground , library = CAST('TRUE' as bit)');
    context={'q':q,'coll_name':college, 'Type':institute_type, 'ins_type':insti_type, 'univ_name':university, 'stand_name':standalone}    
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def university(request):
    result= request.GET['colu']
    return render(request,'university.html',{'colu':result})

def standalone(request):
    return render(request,'standalone.html')

def college_institution(request):
    return render(request,'college_institution.html')


