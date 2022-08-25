# %%
import pandas as pd

# %%
df_accr_u_2017=pd.read_csv("static/csv/2017/accreditation.csv")

# %%
df_accr_u_2017

# %%
def hdd():
    return df_accr_u_2017

# %%
df_uni_accr_u_2017=pd.read_csv("static/csv/2017/university_accreditation.csv")

# %%
df_uni_accr_u_2017

# %%
df_uni_accr_accr_u_2017=pd.merge(df_accr_u_2017,df_uni_accr_u_2017,left_on='id',right_on='accreditation_id',how='inner').drop(['id'],axis=1)

# %%
df_uni_accr_accr_u_2017

# %%
df_uni_u_2017=pd.read_csv("static/csv/2017/university.csv")

# %%
df_uni_u_2017.columns,'infrastructure_id'

# %%
df_uni_accr_merge_u_2017=pd.merge(df_uni_accr_accr_u_2017,df_uni_u_2017 ,left_on='university_id',right_on='id',how='inner').drop(['id'],axis=1)

# %%
df_uni_accr_merge_u_2017

# %%
df_uni_accr_merge_u_2017.info

# %%
df_uni_accr_merge_u_2017['percentage']=(df_uni_accr_merge_u_2017['score'] / df_uni_accr_merge_u_2017['max_score'])*100

# %%
df_uni_accr_merge_u_2017

# %%
df_uni_accr_merge_u_2017['score'].fillna(1,inplace= True)

# %%
df_uni_accr_merge_u_2017['max_score'].fillna(1,inplace= True)

# %%
df_uni_accr_merge_u_2017['percentage'].fillna(1,inplace= True)

# %%
df_uni_accr_merge_u_2017

# %%
df_uni_accr_2017_u_2017 = df_uni_accr_merge_u_2017[['university_id','name','aishe_code','accreditation_body','survey_year_x','has_score','score','max_score','percentage','infrastructure_id']]

# %%
df_uni_accr_2017_u_2017

# %%
df_uni_accr_2017_sort_u_2017 = df_uni_accr_2017_u_2017.sort_values(by='percentage',ascending=False)

# %%
df_uni_accr_2017_sort_u_2017

# %%
df_infr_u_2017=pd.read_csv(("static/csv/2017/infrastructure.csv"),low_memory=False)

# %%
df_infr_u_2017

# %%
df_uni_accr_infr_u_2017=pd.merge(df_uni_accr_2017_sort_u_2017,df_infr_u_2017,left_on='infrastructure_id',right_on='id',how='inner').drop(['id'],axis=1)

# %%
df_uni_accr_infr_u_2017.loc[:,"campus_friendly"]

# %%
df_uni_accr_infr_u_2017.columns                                                                                                                                                         

# %%
df_uni_accr_infrastructure_u_2017=df_uni_accr_infr_u_2017[['university_id','name','aishe_code','accreditation_body','survey_year_x','has_score',
                                             'score','max_score','percentage','infrastructure_id','playground','library','connectivity_nkn',
                                             'laboratory','indoor_stadium','cafeteria','computer_center','campus_friendly']]

# %%
df_uni_accr_infrastructure_u_2017.head(5)

# %%
df_uni_accr_infrastructure_u_2017.playground = df_uni_accr_infrastructure_u_2017.playground.replace({True:1,False:0})

# %%
df_uni_accr_infrastructure_u_2017.playground 

# %%
df_uni_accr_infrastructure_u_2017.library = df_uni_accr_infrastructure_u_2017.playground.replace({True:1,False:0})

# %%
df_uni_accr_infrastructure_u_2017.connectivity_nkn = df_uni_accr_infrastructure_u_2017.connectivity_nkn.replace({True:1,False:0})

# %%
df_uni_accr_infrastructure_u_2017.laboratory = df_uni_accr_infrastructure_u_2017.laboratory.replace({True:1,False:0})

# %%
df_uni_accr_infrastructure_u_2017.indoor_stadium = df_uni_accr_infrastructure_u_2017.indoor_stadium.replace({True:1,False:0})

# %%
df_uni_accr_infrastructure_u_2017.cafeteria = df_uni_accr_infrastructure_u_2017.cafeteria.replace({True:1,False:0})

# %%
df_uni_accr_infrastructure_u_2017.computer_center = df_uni_accr_infrastructure_u_2017.computer_center.replace({True:1,False:0})

# %%
df_uni_accr_infrastructure_u_2017.campus_friendly = df_uni_accr_infrastructure_u_2017.campus_friendly.replace({True:1,False:0})

# %%
df_uni_accr_infrastructure_u_2017

# %%
df_filtered_infra_u_2017 = df_uni_accr_infrastructure_u_2017[['university_id','infrastructure_id','playground','library','connectivity_nkn',	'laboratory','indoor_stadium','cafeteria','computer_center',	'campus_friendly']]

# %%
df_filtered_infra_u_2017

# %%
df_filtered_infra_u_2017['infra_count']=df_filtered_infra_u_2017.playground + df_filtered_infra_u_2017.library + df_filtered_infra_u_2017.connectivity_nkn + df_filtered_infra_u_2017.indoor_stadium + df_filtered_infra_u_2017.laboratory + df_filtered_infra_u_2017.cafeteria + df_filtered_infra_u_2017.computer_center + df_filtered_infra_u_2017.campus_friendly

# %%
df_filtered_infra_u_2017

# %%
find_infra_u_2017=['playground','library','laboratory','indoor_stadium','connectivity_nkn','cafeteria','computer_center','campus_friendly']



# %%
for i in range(len(find_infra_u_2017)):
    print(find_infra_u_2017[i])


    


# %%
df_filtered_infra_u_2017[find_infra_u_2017]

# %%
df_filtered_infra_u_2017[find_infra_u_2017].sum(axis=1)

# %%
def dynamic_infra_sum(df_filtered_infra_u_2017,find_infra_u_2017):
    return df_filtered_infra_u_2017[find_infra_u_2017].sum(axis=1)

    

# %%
df_uni_accr_infrastructure_u_2017['infra_count']=dynamic_infra_sum(df_uni_accr_infrastructure_u_2017,find_infra_u_2017)


# %%
df_uni_accr_infrastructure_u_2017

# %%
df_uni_accr_infrastructure_u_2017[['university_id','accreditation_body','percentage','infra_count']]

# %%
df_uni_accr_infrastructure_sort_u_2017=df_uni_accr_infrastructure_u_2017.sort_values(['percentage','infra_count'],ascending=False)

# %%
df_uni_accr_infrastructure_sort_u_2017

# %%
df_uni_accr_infrastructure_sort_u_2017.head(1)

# %% [markdown]
# examination result

# %%
df_examination_result_u_2017 = pd.read_csv("static/csv/2017/examination_result.csv")

# %%
df_examination_result_u_2017

# %%
df_edu_inst_u_2017=pd.read_csv("static/csv/2017/educational_institution_course.csv")

# %%
df_edu_inst_u_2017

# %%
df_examination_result_merge_u_2017 =pd.merge(df_edu_inst_u_2017,df_examination_result_u_2017,left_on='course_id',right_on='course_id',how='inner',)
df_examination_result_merge_u_2017


# %%
df_examination_result_merge_u_2017.columns

# %%
df_examination_result_merge_filt_u_2017=df_examination_result_merge_u_2017.drop(['id','appeared_female','passed_female','first_class_passed_total','first_class_passed_female','broad_discipline_group_id'],axis= 1)
df_examination_result_merge_filt_u_2017

# %%
df_examination_result_merge_filt_u_2017['pass_percentage']=(df_examination_result_merge_filt_u_2017['passed_total'] / df_examination_result_merge_filt_u_2017['appeared_total'])*100
df_examination_result_merge_filt_u_2017

# %%
df_uni_accr_infra_ex_u_2017=pd.merge(df_examination_result_merge_filt_u_2017,df_uni_accr_infrastructure_sort_u_2017,left_on='institution_id',right_on='university_id').drop(['institution_id'],axis=1)
df_uni_accr_infra_ex_u_2017

# %%
df_uni_accr_infra_exam_u_2017=df_uni_accr_infra_ex_u_2017.sort_values(['percentage','infra_count','pass_percentage'],ascending=False)
df_uni_accr_infra_exam_u_2017

# %%
df_uni_accr_infra_exam_sort_u_2017=df_uni_accr_infra_exam_u_2017[[ 'university_id','name', 'state_code','department_id','discipline', 'faculty_id',  'course_id', 'survey_year','examination_result_id', 'percentage','infra_count','pass_percentage']]

# %%
df_uni_accr_infra_exam_sort_u_2017.head(20)

# %%



