import pandas as pd
from django.db import connection
from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse
from .models import CollegeInstitution, CollegeInstitutionAccreditation, RefInstituteType, StandaloneInstitution, University
from django.http import JsonResponse
import pandas as pd
import json
from neww import hdd
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

def about(request):
    return render(request,'about.html')

def university(request):
    university=University.objects.all()
    university_name=request.GET.get('university_name')
    context={'university_name':university_name, 'univ_name':university}    
    return render(request,'university.html',context)

def standalone_institution(request):
    standalone=StandaloneInstitution.objects.all()
    standalone_name=request.GET.get('standalone_name')
    context={'standalone_name':standalone_name,'stand_name':standalone}    
    return render(request,'standalone_institution.html',context)

def college_institution(request):
    college=CollegeInstitution.objects.all()
    college_name= request.GET.get('college_name')
    college_institution_result=CollegeInstitution.objects.raw(' SELECT college_institution.id, college_institution.name, course.discipline,examination_result.result, educational_institution_course.course_id FROM college_institution , course, educational_institution_course, examination_result WHERE (educational_institution_course.course_id= examination_result.course_id) AND (examination_result.course_id=course.id) AND (educational_institution_course.institution_id= college_institution.id) ORDER BY result DESC');
    college_exam1=request.GET.get('college_exam')
    context={'college_exam':college_exam1, 'coll_name':college, 'college_name':college_name, 'college_institution_result': college_institution_result}    
    return render(request,'college_institution.html',context)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def courses(request):
    return render(request,'courses.html')

def accreditation_college_institution(request):
    return render(request,'accreditation_college_institution.html')

def accreditation_standalone_institution(request):
    return render(request,'accreditation_standalone_institution.html')

def accreditation_university(request):
    top10univacc2019=pd.read_csv("static/csv/top_10_accreditation_2019.csv")
    json_records = top10univacc2019.reset_index().to_json(orient ='records')
    univacc2019 = []
    univacc2019 = json.loads(json_records)
    top10univacc2018=pd.read_csv("static/csv/top_10_accreditation_2018.csv")
    json_records = top10univacc2018.reset_index().to_json(orient ='records')
    univacc2018 = []
    univacc2018 = json.loads(json_records)
    
    top10univacc2017=pd.read_csv("static/csv/top_10_accreditation_2017.csv")
    json_records = top10univacc2017.reset_index().to_json(orient ='records')
    univacc2017 = []
    univacc2017 = json.loads(json_records)
    
    year_type= request.GET.get('year_type')
    context={'univacc2019':univacc2019,'univacc2018':univacc2018,'univacc2017':univacc2017,'year_type':year_type}
    return render(request,'accreditation_university.html',context)

def infrastructure_college_institution(request):
    return render(request,'infrastructure_college_institution.html')

def infrastructure_standalone_institution(request):
    return render(request,'infrastructure_standalone_institution.html')

def infrastructure_university(request):
    return render(request,'infrastructure_university.html')

def examination_result_college_institution(request):
    return render(request,'examination_result_college_institution.html')

def examination_result_standalone_institution(request):
    return render(request,'examination_result_standalone_institution.html')

def examination_result_university(request):
    return render(request,'examination_result_university.html')

def sfr_college_institution(request):
    return render(request,'sfr_college_institution.html')

def sfr_standalone_institution(request):
    return render(request,'sfr_standalone_institution.html')

def sfr_university(request):
    return render(request,'sfr_university.html')

def placement_college_institution(request):
    return render(request,'placement_college_institution.html')

def placement_standalone_institution(request):
    return render(request,'placement_standalone_institution.html')

def placement_university(request):
    return render(request,'accreditation_university.html')

def choose_multiple_parameters_college_institution(request):
    return render(request,'choose_multiple_parameters_college_institution.html')

def choose_multiple_parameters_standalone_institution(request):
    return render(request,'choose_multiple_parameters_standalone_institution.html')

def choose_multiple_parameters_university(request):
    return render(request,'choose_multiple_parameters_university.html')

def start(request):
    return render(request,'start.html')

def accreditation_infrastructure(request):
    find_infra=['playground','library','laboratory','indoor_stadium','connectivity_nkn','cafeteria','computer_center','campus_friendly']
    df_accr= pd.read_csv("static/csv/2019/accreditation.csv")
    df_uni_accr=pd.read_csv("static/csv/2019/university_accreditation.csv")
    df_uni_accr_accr=pd.merge(df_accr,df_uni_accr,left_on='id',right_on='accreditation_id',how='inner').drop(['id'],axis=1)
    df_uni=pd.read_csv("static/csv/2019/university.csv")
    df_uni_accr_merge=pd.merge(df_uni_accr_accr,df_uni,left_on='university_id',right_on='id',how='inner').drop(['id'],axis=1)
    df_uni_accr_merge['percentage']=(df_uni_accr_merge['score'] / df_uni_accr_merge['max_score'])*100
    df_uni_accr_merge['score'].fillna(1,inplace= True)
    df_uni_accr_merge['max_score'].fillna(1,inplace= True)
    df_uni_accr_merge['percentage'].fillna(1,inplace= True)
    df_uni_accr_2019=df_uni_accr_merge[['university_id','name','aishe_code','accreditation_body','survey_year_x','has_score','score','max_score','percentage','infrastructure_id']]
    df_uni_accr_2019_sort=df_uni_accr_2019.sort_values(by='percentage',ascending=False)
    df_infr=pd.read_csv("static/csv/2019/infrastructure.csv")
    df_uni_accr_infr=pd.merge(df_uni_accr_2019_sort,df_infr,left_on='infrastructure_id',right_on='id',how='inner').drop(['id'],axis=1)
    df_uni_accr_infrastructure=df_uni_accr_infr[['university_id','name','aishe_code','accreditation_body','survey_year_x','has_score',
                                                'score','max_score','percentage','infrastructure_id','playground','library','connectivity_nkn',
                                                'laboratory','indoor_stadium','cafeteria','computer_center','campus_friendly']]
    df_uni_accr_infrastructure.playground = df_uni_accr_infrastructure.playground.replace({True:1,False:0})
    df_uni_accr_infrastructure.library = df_uni_accr_infrastructure.playground.replace({True:1,False:0})
    df_uni_accr_infrastructure.connectivity_nkn = df_uni_accr_infrastructure.connectivity_nkn.replace({True:1,False:0})
    df_uni_accr_infrastructure.laboratory = df_uni_accr_infrastructure.laboratory.replace({True:1,False:0})
    df_uni_accr_infrastructure.indoor_stadium = df_uni_accr_infrastructure.indoor_stadium.replace({True:1,False:0})
    df_uni_accr_infrastructure.cafeteria = df_uni_accr_infrastructure.cafeteria.replace({True:1,False:0})
    df_uni_accr_infrastructure.computer_center = df_uni_accr_infrastructure.computer_center.replace({True:1,False:0})
    df_uni_accr_infrastructure.campus_friendly = df_uni_accr_infrastructure.campus_friendly.replace({True:1,False:0})
    df_filtered_infra= df_uni_accr_infrastructure[['university_id','infrastructure_id','playground','library','connectivity_nkn',	'laboratory','indoor_stadium','cafeteria','computer_center',	'campus_friendly']]
    df_filtered_infra['infra_count']=df_filtered_infra.playground + df_filtered_infra.library + df_filtered_infra.connectivity_nkn + df_filtered_infra.indoor_stadium + df_filtered_infra.laboratory + df_filtered_infra.cafeteria + df_filtered_infra.computer_center + df_filtered_infra.campus_friendly
    
    
    for i in range(len(find_infra)):
        print(find_infra[i])
    df_filtered_infra[find_infra].sum(axis=1)
    def dynamic_infra_sum(df_filtered_infra,find_infra):
        return df_filtered_infra[find_infra].sum(axis=1)
    df_uni_accr_infrastructure['infra_count']=dynamic_infra_sum(df_uni_accr_infrastructure,find_infra)
    df_uni_accr_infrastructure_sort=df_uni_accr_infrastructure.sort_values(['percentage','infra_count'],ascending=False)
    df_uni_accr_infrastructure_sort.playground = df_uni_accr_infrastructure_sort.playground.replace({1:'Yes',0:'No'})
    df_uni_accr_infrastructure_sort.library = df_uni_accr_infrastructure_sort.playground.replace({1:'Yes',0:'No'})
    df_uni_accr_infrastructure_sort.connectivity_nkn = df_uni_accr_infrastructure_sort.connectivity_nkn.replace({1:'Yes',0:'No'})
    df_uni_accr_infrastructure_sort.laboratory = df_uni_accr_infrastructure_sort.laboratory.replace({1:'Yes',0:'No'})
    df_uni_accr_infrastructure_sort.indoor_stadium = df_uni_accr_infrastructure_sort.indoor_stadium.replace({1:'Yes',0:'No'})
    df_uni_accr_infrastructure_sort.cafeteria = df_uni_accr_infrastructure_sort.cafeteria.replace({1:'Yes',0:'No'})
    df_uni_accr_infrastructure_sort.computer_center = df_uni_accr_infrastructure_sort.computer_center.replace({1:'Yes',0:'No'})
    df_uni_accr_infrastructure_sort.campus_friendly = df_uni_accr_infrastructure_sort.campus_friendly.replace({1:'Yes',0:'No'})
    obje=df_uni_accr_infrastructure_sort.to_html()
    df=hdd()
    ffd= df.to_html()
    context={'obje':obje}    
    return HttpResponse(ffd)