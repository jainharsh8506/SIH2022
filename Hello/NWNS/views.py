from http.client import HTTPResponse
from unicodedata import name
from django.shortcuts import render, HttpResponse
from .models import RefInstituteType , College, CollegeInstitution
from django.http import JsonResponse

# Create your views here.

def index(request):
    college=CollegeInstitution.objects.raw('Select id,address_line1, address_line2,city,name,website,pin_code from college_institution')
    name = request.GET.get('name', None)
    results = request.GET.get('results', None)
    col=College.objects.filter(name=results)
    context={'college':college , 'name':name, 'col':col}
    
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def university(request):
    return render(request,'university.html')

def standalone(request):
    return render(request,'standalone.html')

def college_institution(request):
    return render(request,'college_institution.html')



