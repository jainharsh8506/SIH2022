from http.client import HTTPResponse
from unicodedata import name
from django.shortcuts import render, HttpResponse
from .models import RefInstituteType , College
from django.http import JsonResponse

# Create your views here.

def index(request):
    college=College.objects.all()
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



