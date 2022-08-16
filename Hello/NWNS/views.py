from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse
from .models import RefInstituteType , College
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def university(request):
    return render(request,'university.html')

def standalone(request):
    return render(request,'standalone.html')

def college_institution(request):
    return render(request,'college_institution.html')


