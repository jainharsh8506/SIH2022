from http.client import HTTPResponse
from unicodedata import name
from django.shortcuts import render, HttpResponse
from .models import InstituteTypeName, RefInstituteType , College, CollegeInstitution, StandaloneInstitution, University
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
    context={'coll_name':college, 'Type':institute_type, 'ins_type':insti_type, 'univ_name':university, 'stand_name':standalone}    
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


