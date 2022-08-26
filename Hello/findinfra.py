# %%
import pandas as pd

# %%
df_accr_u_2019=pd.read_csv("static/csv/2019/accreditation.csv")

# %%
df_accr_u_2019

# %%
df_uni_accr_u_2019=pd.read_csv("static/csv/2019/university_accreditation.csv")

# %%
df_uni_accr_u_2019

# %%
df_uni_accr_accr_u_2019=pd.merge(df_accr_u_2019,df_uni_accr_u_2019,left_on='id',right_on='accreditation_id',how='inner').drop(['id'],axis=1)

# %%
df_uni_accr_accr_2019_u_2019=pd.merge(df_accr_u_2019,df_uni_accr_u_2019,left_on='id',right_on='accreditation_id',how='inner').drop(['id'],axis=1)

# %%
df_uni_accr_accr_u_2019

# %%
df_uni_u_2019=pd.read_csv("static/csv/2019/university.csv")

# %%
df_uni_u_2019.columns,'infrastructure_id'

# %%
df_uni_accr_merge_u_2019=pd.merge(df_uni_accr_accr_u_2019,df_uni_u_2019,left_on='university_id',right_on='id',how='inner').drop(['id'],axis=1)

# %%
df_uni_accr_merge_u_2019=pd.merge(df_uni_accr_accr_2019_u_2019,df_uni_u_2019,left_on='university_id',right_on='id',how='inner').drop(['id'],axis=1)

# %%
df_uni_accr_merge_u_2019

# %%
df_uni_accr_merge_u_2019.info

# %%
df_uni_accr_merge_u_2019['percentage']=(df_uni_accr_merge_u_2019['score'] / df_uni_accr_merge_u_2019['max_score'])*100

# %%
df_uni_accr_merge_u_2019

# %%
df_uni_accr_merge_u_2019['score'].fillna(1,inplace= True)

# %%
df_uni_accr_merge_u_2019['max_score'].fillna(1,inplace= True)

# %%
df_uni_accr_merge_u_2019['percentage'].fillna(1,inplace= True)

# %%
df_uni_accr_merge_u_2019

# %%
df_uni_accr_u_2019=df_uni_accr_merge_u_2019[['university_id','name','aishe_code','accreditation_body','survey_year_x','has_score','score','max_score','percentage','infrastructure_id']]

# %%
df_uni_accr_u_2019

# %%
df_uni_accr_u_2019_sort=df_uni_accr_u_2019.sort_values(by='percentage',ascending=False)

# %%
df_uni_accr_u_2019_sort.head(10)

# %%
df_uni_accr_u_2019_sort.head(10).to_csv("top_10_accreditation_2019")

# %%
df_infr_u_2019=pd.read_csv("static/csv/2019/infrastructure.csv")

# %%
df_infr_u_2019

# %%
df_uni_accr_infr_u_2019=pd.merge(df_uni_accr_u_2019_sort,df_infr_u_2019,left_on='infrastructure_id',right_on='id',how='inner').drop(['id'],axis=1)

# %%
df_uni_accr_infr_u_2019.loc[:,"campus_friendly"]

# %%
df_uni_accr_infr_u_2019.columns                                                                                                                                                         

# %%
df_uni_accr_infrastructure_u_2019=df_uni_accr_infr_u_2019[['university_id','name','aishe_code','accreditation_body','survey_year_x','has_score',
                                             'score','max_score','percentage','infrastructure_id','playground','library','connectivity_nkn',
                                             'laboratory','indoor_stadium','cafeteria','computer_center','campus_friendly']]

# %%
df_uni_accr_infrastructure_u_2019.head(5)

# %%
df_uni_accr_infrastructure_u_2019.playground = df_uni_accr_infrastructure_u_2019.playground.replace({True:1,False:0})

# %%
df_uni_accr_infrastructure_u_2019.playground 

# %%
df_uni_accr_infrastructure_u_2019.library = df_uni_accr_infrastructure_u_2019.playground.replace({True:1,False:0})

# %%
df_uni_accr_infrastructure_u_2019.connectivity_nkn = df_uni_accr_infrastructure_u_2019.connectivity_nkn.replace({True:1,False:0})

# %%
df_uni_accr_infrastructure_u_2019.laboratory = df_uni_accr_infrastructure_u_2019.laboratory.replace({True:1,False:0})

# %%
df_uni_accr_infrastructure_u_2019.indoor_stadium = df_uni_accr_infrastructure_u_2019.indoor_stadium.replace({True:1,False:0})

# %%
df_uni_accr_infrastructure_u_2019.cafeteria = df_uni_accr_infrastructure_u_2019.cafeteria.replace({True:1,False:0})

# %%
df_uni_accr_infrastructure_u_2019.computer_center = df_uni_accr_infrastructure_u_2019.computer_center.replace({True:1,False:0})

# %%
df_uni_accr_infrastructure_u_2019.campus_friendly = df_uni_accr_infrastructure_u_2019.campus_friendly.replace({True:1,False:0})

# %%
df_uni_accr_infrastructure_u_2019

# %%
df_filtered_infra_u_2019 = df_uni_accr_infrastructure_u_2019[['university_id','infrastructure_id','playground','library','connectivity_nkn',	'laboratory','indoor_stadium','cafeteria','computer_center',	'campus_friendly']]

# %%
df_filtered_infra_u_2019

# %%
df_filtered_infra_u_2019['infra_count']=df_filtered_infra_u_2019["playground"] + df_filtered_infra_u_2019["library"]+ df_filtered_infra_u_2019["connectivity_nkn"] + df_filtered_infra_u_2019["indoor_stadium"] + df_filtered_infra_u_2019["laboratory"] + df_filtered_infra_u_2019["cafeteria"] + df_filtered_infra_u_2019["computer_center"] + df_filtered_infra_u_2019["campus_friendly"]

# %%
df_filtered_infra_u_2019

# %%
find_infra=['playground','library','laboratory','indoor_stadium','connectivity_nkn','cafeteria','computer_center','campus_friendly']



# %%
for i in range(len(find_infra)):
    print(find_infra[i])


    


# %%
df_filtered_infra_u_2019[find_infra]

# %%
df_filtered_infra_u_2019[find_infra].sum(axis=1)

# %%
def dynamic_infra_sum(df_filtered_infra_u_2019,find_infra):
    return df_filtered_infra_u_2019[find_infra].sum(axis=1)

    

# %%
df_uni_accr_infrastructure_u_2019['infra_count']=dynamic_infra_sum(df_uni_accr_infrastructure_u_2019,find_infra)


# %%
df_uni_accr_infrastructure_u_2019

# %%
df_uni_accr_infrastructure_u_2019[['university_id','accreditation_body','percentage','infra_count']]

# %%
df_uni_accr_infrastructure_sort_u_2019=df_uni_accr_infrastructure_u_2019.sort_values(['percentage','infra_count'],ascending=False)

# %%
df_uni_accr_infrastructure_sort_u_2019

# %%
df_uni_accr_infrastructure_sort_u_2019.head(1)

# %% [markdown]
# examination result

# %%
df_examination_result_u_2019 = pd.read_csv("static/csv/2019/examination_result.csv")

# %%
df_edu_inst_u_2019=pd.read_csv("static/csv/2019/educational_institution_course.csv")

# %%
df_edu_inst_u_2019

# %%
df_examination_result_u_2019

# %%
df_examination_result_merge_u_2019 =pd.merge(df_edu_inst_u_2019,df_examination_result_u_2019,left_on='course_id',right_on='course_id',how='inner',)

# %%
df_examination_result_merge_u_2019

# %%
df_examination_result_merge_u_2019.columns

# %%
df_examination_result_merge_filt_u_2019=df_examination_result_merge_u_2019.drop(['id','appeared_female','passed_female','first_class_passed_total','first_class_passed_female','broad_discipline_group_id'],axis= 1)
df_examination_result_merge_filt_u_2019

# %%
df_examination_result_merge_filt_u_2019['pass_percentage']=(df_examination_result_merge_filt_u_2019['passed_total'] / df_examination_result_merge_filt_u_2019['appeared_total'])*100
df_examination_result_merge_filt_u_2019

# %%
df_uni_accr_infra_ex_u_2019=pd.merge(df_examination_result_merge_filt_u_2019,df_uni_accr_infrastructure_sort_u_2019,left_on='institution_id',right_on='university_id').drop(['institution_id'],axis=1)
df_uni_accr_infra_ex_u_2019

# %%
df_uni_accr_infra_ex_u_2019.columns

# %%
df_uni_accr_infra_exam_u_2019=df_uni_accr_infra_ex_u_2019.sort_values(['percentage','infra_count','pass_percentage'],ascending=False)
df_uni_accr_infra_exam_u_2019

# %%
df_uni_accr_infra_exam_u_2019['infrastructure']=(df_uni_accr_infra_exam_u_2019['infra_count']/8)*100
df_uni_accr_infra_exam_u_2019

# %%
df_uni_accr_infrastructure_u_2019=df_uni_accr_infra_exam_u_2019[[ 'university_id','name', 'state_code','department_id','discipline', 'faculty_id',  'course_id', 'survey_year','examination_result_id','infra_count','infrastructure','percentage','pass_percentage']]

# %%
df_uni_accr_infrastructure_u_2019

# %%
df_uni_disc_com_u_2019=df_uni_accr_infrastructure_u_2019.loc[df_uni_accr_infrastructure_u_2019['discipline']=='Computer Science']

# %%
df_uni_disc_com_u_2019

# %%
df_uni_disc_com_u_2019['percentage']

# %%
df_uni_disc_com_u_2019[['percentage','infrastructure','pass_percentage']].mean(axis=1)


# %% [markdown]
# percentage=int(input())
# infra_count=int(input())
# pass_percentage= int(input())
# def average():
#     
# 

# %%
df_uni_disc_com_u_2019['combined']=df_uni_disc_com_u_2019[['percentage','infrastructure','pass_percentage']].mean(axis=1)
df_uni_disc_com_u_2019.sort_values(['combined'],ascending=False)

# %%
slider_arr=[20,50,30]
for i in range(len(slider_arr)):
    slider_arr[i]/=100

    

df_uni_disc_com_u_2019['user_defined_score']=(df_uni_disc_com_u_2019['percentage']*slider_arr[0] + df_uni_disc_com_u_2019['infrastructure']*slider_arr[1] + df_uni_disc_com_u_2019['pass_percentage']*slider_arr[2])

# %%
df_uni_disc_com_u_2019=df_uni_disc_com_u_2019.sort_values(['user_defined_score'],ascending=False)
df_uni_disc_com_u_2019

# %%
df_uni_arranged_u_2019=df_uni_disc_com_u_2019[[ 'university_id','name', 'state_code','department_id','discipline', 'faculty_id',  'course_id', 'survey_year','examination_result_id','infra_count','infrastructure','percentage','pass_percentage','combined','user_defined_score']]
df_uni_arranged_u_2019

# %%
df_uni_arranged_u_2019.to_csv("Overall_combined_result_2017.csv")

# %%



