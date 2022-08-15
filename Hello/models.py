# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Accreditation(models.Model):
    id = models.IntegerField(primary_key=True)
    accreditation_body = models.CharField(max_length=-1)
    score = models.FloatField(blank=True, null=True)
    max_score = models.FloatField(blank=True, null=True)
    has_score = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'accreditation'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class College(models.Model):
    aishe_code = models.CharField(max_length=-1)
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=-1)
    university = models.ForeignKey('RefUniversity', models.DO_NOTHING)
    district_code = models.CharField(max_length=-1)
    state_code = models.ForeignKey('RefDistrict', models.DO_NOTHING, db_column='state_code')
    type = models.ForeignKey('RefUniversityCollegeType', models.DO_NOTHING)
    survey_year = models.IntegerField()
    is_dcf_applicable = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'college'
        unique_together = (('id', 'survey_year'),)


class Department(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'department'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Faculty(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'faculty'


class PersonsCountByCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    total_general_total = models.IntegerField(blank=True, null=True)
    total_general_females = models.IntegerField(blank=True, null=True)
    total_sc_total = models.IntegerField(blank=True, null=True)
    total_sc_females = models.IntegerField(blank=True, null=True)
    total_st_total = models.IntegerField(blank=True, null=True)
    total_st_females = models.IntegerField(blank=True, null=True)
    total_obc_total = models.IntegerField(blank=True, null=True)
    total_obc_females = models.IntegerField(blank=True, null=True)
    total_total_persons = models.IntegerField(blank=True, null=True)
    total_total_females = models.IntegerField(blank=True, null=True)
    total_remarks = models.ForeignKey('RefCountByCategoryRemarks', models.DO_NOTHING, blank=True, null=True)
    pwd_general_total = models.IntegerField(blank=True, null=True)
    pwd_general_females = models.IntegerField(blank=True, null=True)
    pwd_sc_total = models.IntegerField(blank=True, null=True)
    pwd_sc_females = models.IntegerField(blank=True, null=True)
    pwd_st_total = models.IntegerField(blank=True, null=True)
    pwd_st_females = models.IntegerField(blank=True, null=True)
    pwd_obc_total = models.IntegerField(blank=True, null=True)
    pwd_obc_females = models.IntegerField(blank=True, null=True)
    pwd_total_persons = models.IntegerField(blank=True, null=True)
    pwd_total_females = models.IntegerField(blank=True, null=True)
    pwd_remarks = models.ForeignKey('RefCountByCategoryRemarks', models.DO_NOTHING, blank=True, null=True)
    muslim_minority_general_total = models.IntegerField(blank=True, null=True)
    muslim_minority_general_females = models.IntegerField(blank=True, null=True)
    muslim_minority_sc_total = models.IntegerField(blank=True, null=True)
    muslim_minority_sc_females = models.IntegerField(blank=True, null=True)
    muslim_minority_st_total = models.IntegerField(blank=True, null=True)
    muslim_minority_st_females = models.IntegerField(blank=True, null=True)
    muslim_minority_obc_total = models.IntegerField(blank=True, null=True)
    muslim_minority_obc_females = models.IntegerField(blank=True, null=True)
    muslim_minority_total_persons = models.IntegerField(blank=True, null=True)
    muslim_minority_total_females = models.IntegerField(blank=True, null=True)
    muslim_minority_remarks = models.ForeignKey('RefCountByCategoryRemarks', models.DO_NOTHING, blank=True, null=True)
    other_minority_general_total = models.IntegerField(blank=True, null=True)
    other_minority_general_females = models.IntegerField(blank=True, null=True)
    other_minority_sc_total = models.IntegerField(blank=True, null=True)
    other_minority_sc_females = models.IntegerField(blank=True, null=True)
    other_minority_st_total = models.IntegerField(blank=True, null=True)
    other_minority_st_females = models.IntegerField(blank=True, null=True)
    other_minority_obc_total = models.IntegerField(blank=True, null=True)
    other_minority_obc_females = models.IntegerField(blank=True, null=True)
    other_minority_total_persons = models.IntegerField(blank=True, null=True)
    other_minority_total_females = models.IntegerField(blank=True, null=True)
    other_minority_remarks = models.ForeignKey('RefCountByCategoryRemarks', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'persons_count_by_category'


class RefBroadDisciplineGroup(models.Model):
    id = models.CharField(primary_key=True, max_length=-1)
    category = models.ForeignKey('RefBroadDisciplineGroupCategory', models.DO_NOTHING)
    discipline_group = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'ref_broad_discipline_group'


class RefBroadDisciplineGroupCategory(models.Model):
    id = models.CharField(primary_key=True, max_length=-1)
    discipline_group_category = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'ref_broad_discipline_group_category'


class RefCollegeInstitutionStatutoryBody(models.Model):
    id = models.CharField(primary_key=True, max_length=-1)
    statutory_body = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'ref_college_institution_statutory_body'


class RefCountByCategoryRemarks(models.Model):
    id = models.CharField(primary_key=True, max_length=-1)
    statutory_body = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'ref_count_by_category_remarks'


class RefCountry(models.Model):
    country_id = models.IntegerField(primary_key=True)
    country_code = models.CharField(max_length=-1)
    country_name = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'ref_country'


class RefCourseLevel(models.Model):
    id = models.CharField(primary_key=True, max_length=-1)
    level = models.CharField(max_length=-1)
    name = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'ref_course_level'


class RefCourseMode(models.Model):
    id = models.CharField(primary_key=True, max_length=-1)
    mode = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'ref_course_mode'


class RefCourseType(models.Model):
    id = models.CharField(primary_key=True, max_length=-1)
    type = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'ref_course_type'


class RefDiplomaCourse(models.Model):
    id = models.CharField(primary_key=True, max_length=-1)
    type = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'ref_diploma_course'


class RefDistrict(models.Model):
    dist_code = models.CharField(max_length=-1)
    st_code = models.CharField(primary_key=True, max_length=-1)
    name = models.CharField(max_length=-1)
    sno = models.IntegerField()
    lgd_district_code = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ref_district'
        unique_together = (('st_code', 'dist_code'),)


class RefExaminationSystem(models.Model):
    id = models.CharField(primary_key=True, max_length=-1)
    system = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'ref_examination_system'


class RefInstituteType(models.Model):
    id = models.CharField(primary_key=True, max_length=-1)
    name = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'ref_institute_type'


class RefInstitutionManagement(models.Model):
    id = models.CharField(primary_key=True, max_length=-1)
    management = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'ref_institution_management'


class RefNonTeachingStaffGroup(models.Model):
    id = models.CharField(primary_key=True, max_length=-1)
    staff_group = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'ref_non_teaching_staff_group'


class RefNonTeachingStaffType(models.Model):
    id = models.CharField(primary_key=True, max_length=-1)
    staff_type = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'ref_non_teaching_staff_type'


class RefProgramme(models.Model):
    id = models.CharField(primary_key=True, max_length=-1)
    programme = models.CharField(max_length=-1)
    course_level = models.ForeignKey(RefCourseLevel, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ref_programme'


class RefProgrammeBroadDisciplineGroupAndCategory(models.Model):
    programme = models.ForeignKey(RefProgramme, models.DO_NOTHING)
    broad_discipline_group_category = models.ForeignKey(RefBroadDisciplineGroupCategory, models.DO_NOTHING)
    broad_discipline_group = models.ForeignKey(RefBroadDisciplineGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ref_programme_broad_discipline_group_and_category'


class RefProgrammeStatutoryBody(models.Model):
    id = models.CharField(primary_key=True, max_length=-1)
    statutory_body = models.CharField(max_length=-1)
    valid_for_form2 = models.BooleanField()
    valid_for_form3 = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'ref_programme_statutory_body'


class RefSpeciality(models.Model):
    id = models.CharField(primary_key=True, max_length=-1)
    speciality = models.CharField(max_length=-1)
    valid_for_form1 = models.BooleanField()
    valid_for_form2 = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'ref_speciality'


class RefStandaloneInstitution(models.Model):
    aishe_code = models.CharField(primary_key=True, max_length=-1)
    statecode = models.ForeignKey('RefState', models.DO_NOTHING, db_column='statecode')
    name = models.CharField(max_length=-1)
    id = models.IntegerField()
    statebodyid = models.ForeignKey('RefStateBody', models.DO_NOTHING, db_column='statebodyid')
    survey_year = models.IntegerField()
    district_code = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ref_standalone_institution'


class RefState(models.Model):
    st_code = models.CharField(primary_key=True, max_length=-1)
    name = models.CharField(max_length=-1)
    lgd_code = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ref_state'


class RefStateBody(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'ref_state_body'


class RefStudentHostelType(models.Model):
    id = models.CharField(primary_key=True, max_length=-1)
    type = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'ref_student_hostel_type'


class RefTeachingStaffDesignation(models.Model):
    id = models.CharField(primary_key=True, max_length=-1)
    designation = models.CharField(max_length=-1)
    valid_for_form1 = models.BooleanField()
    valid_for_form2 = models.BooleanField()
    valid_for_form3 = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'ref_teaching_staff_designation'


class RefTeachingStaffSelectionMode(models.Model):
    id = models.CharField(primary_key=True, max_length=-1)
    selection_mode = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'ref_teaching_staff_selection_mode'


class RefUniversity(models.Model):
    aishe_code = models.CharField(max_length=-1)
    id = models.CharField(primary_key=True, max_length=-1)
    name = models.CharField(max_length=-1)
    statecode = models.ForeignKey(RefState, models.DO_NOTHING, db_column='statecode')
    survey_year = models.IntegerField()
    is_dcf_applicable = models.BooleanField()
    type = models.ForeignKey('RefUniversityType', models.DO_NOTHING)
    district_code = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'ref_university'
        unique_together = (('id', 'survey_year'),)


class RefUniversityCollegeType(models.Model):
    id = models.CharField(primary_key=True, max_length=-1)
    type = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'ref_university_college_type'


class RefUniversityType(models.Model):
    id = models.CharField(primary_key=True, max_length=-1)
    type = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'ref_university_type'
