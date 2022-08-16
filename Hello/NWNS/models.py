# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class RefBroadDisciplineGroupCategory(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    discipline_group_category = models.CharField(max_length=250)

    class Meta:
        managed = True
        db_table = 'ref_broad_discipline_group_category'


class RefBroadDisciplineGroup(models.Model):
    id = models.CharField(primary_key=True, max_length=-1)
    category = models.ForeignKey('RefBroadDisciplineGroupCategory', models.DO_NOTHING)
    discipline_group = models.CharField(max_length=-1)

    class Meta:
        managed = True
        db_table = 'ref_broad_discipline_group'


class RefCollegeInstitutionStatutoryBody(models.Model):
    id = models.CharField(primary_key=True, max_length=-1)
    statutory_body = models.CharField(max_length=-1)

    class Meta:
        managed = True
        db_table = 'ref_college_institution_statutory_body'


class RefCountByCategoryRemarks(models.Model):
    id = models.CharField(primary_key=True, max_length=-1)
    statutory_body = models.CharField(max_length=-1)

    class Meta:
        managed = True
        db_table = 'ref_count_by_category_remarks'


class RefCountry(models.Model):
    country_id = models.IntegerField(primary_key=True)
    country_code = models.CharField(max_length=-1)
    country_name = models.CharField(max_length=-1)

    class Meta:
        managed = True
        db_table = 'ref_country'


class RefCourseLevel(models.Model):
    id = models.CharField(primary_key=True, max_length=-1)
    level = models.CharField(max_length=-1)
    name = models.CharField(max_length=-1)

    class Meta:
        managed = True
        db_table = 'ref_course_level'


class RefCourseMode(models.Model):
    id = models.CharField(primary_key=True, max_length=-1)
    mode = models.CharField(max_length=-1)

    class Meta:
        managed = True
        db_table = 'ref_course_mode'


class RefCourseType(models.Model):
    id = models.CharField(primary_key=True, max_length=-1)
    type = models.CharField(max_length=-1)

    class Meta:
        managed = True
        db_table = 'ref_course_type'


class RefDiplomaCourse(models.Model):
    id = models.CharField(primary_key=True, max_length=-1)
    type = models.CharField(max_length=-1)

    class Meta:
        managed = True
        db_table = 'ref_diploma_course'


class RefDistrict(models.Model):
    dist_code = models.CharField(max_length=-1)
    st_code = models.CharField(primary_key=True, max_length=-1)
    name = models.CharField(max_length=-1)
    sno = models.IntegerField()
    lgd_district_code = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'ref_district'
        unique_together = (('st_code', 'dist_code'),)


class RefExaminationSystem(models.Model):
    id = models.CharField(primary_key=True, max_length=-1)
    system = models.CharField(max_length=-1)

    class Meta:
        managed = True
        db_table = 'ref_examination_system'


class RefInstituteType(models.Model):
    id = models.CharField(primary_key=True, max_length=-1)
    name = models.CharField(max_length=-1)

    class Meta:
        managed = True
        db_table = 'ref_institute_type'


class RefInstitutionManagement(models.Model):
    id = models.CharField(primary_key=True, max_length=-1)
    management = models.CharField(max_length=-1)

    class Meta:
        managed = True
        db_table = 'ref_institution_management'


class RefNonTeachingStaffGroup(models.Model):
    id = models.CharField(primary_key=True, max_length=-1)
    staff_group = models.CharField(max_length=-1)

    class Meta:
        managed = True
        db_table = 'ref_non_teaching_staff_group'


class RefNonTeachingStaffType(models.Model):
    id = models.CharField(primary_key=True, max_length=-1)
    staff_type = models.CharField(max_length=-1)

    class Meta:
        managed = True
        db_table = 'ref_non_teaching_staff_type'


class RefProgramme(models.Model):
    id = models.CharField(primary_key=True, max_length=-1)
    programme = models.CharField(max_length=-1)
    course_level = models.ForeignKey(RefCourseLevel, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'ref_programme'


class RefProgrammeBroadDisciplineGroupAndCategory(models.Model):
    programme = models.ForeignKey(RefProgramme, models.DO_NOTHING)
    broad_discipline_group_category = models.ForeignKey(RefBroadDisciplineGroupCategory, models.DO_NOTHING)
    broad_discipline_group = models.ForeignKey(RefBroadDisciplineGroup, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'ref_programme_broad_discipline_group_and_category'


class RefProgrammeStatutoryBody(models.Model):
    id = models.CharField(primary_key=True, max_length=-1)
    statutory_body = models.CharField(max_length=-1)
    valid_for_form2 = models.BooleanField()
    valid_for_form3 = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'ref_programme_statutory_body'


class RefSpeciality(models.Model):
    id = models.CharField(primary_key=True, max_length=-1)
    speciality = models.CharField(max_length=-1)
    valid_for_form1 = models.BooleanField()
    valid_for_form2 = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'ref_speciality'


class RefState(models.Model):
    st_code = models.CharField(primary_key=True, max_length=-1)
    name = models.CharField(max_length=-1)
    lgd_code = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'ref_state'


class RefStateBody(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=-1)

    class Meta:
        managed = True
        db_table = 'ref_state_body'


class RefStandaloneInstitution(models.Model):
    aishe_code = models.CharField(primary_key=True, max_length=-1)
    statecode = models.ForeignKey('RefState', models.DO_NOTHING, db_column='statecode')
    name = models.CharField(max_length=-1)
    id = models.IntegerField()
    statebodyid = models.ForeignKey('RefStateBody', models.DO_NOTHING, db_column='statebodyid')
    survey_year = models.IntegerField()
    district_code = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ref_standalone_institution'


class RefStudentHostelType(models.Model):
    id = models.CharField(primary_key=True, max_length=-1)
    type = models.CharField(max_length=-1)

    class Meta:
        managed = True
        db_table = 'ref_student_hostel_type'


class RefTeachingStaffDesignation(models.Model):
    id = models.CharField(primary_key=True, max_length=-1)
    designation = models.CharField(max_length=-1)
    valid_for_form1 = models.BooleanField()
    valid_for_form2 = models.BooleanField()
    valid_for_form3 = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'ref_teaching_staff_designation'


class RefTeachingStaffSelectionMode(models.Model):
    id = models.CharField(primary_key=True, max_length=-1)
    selection_mode = models.CharField(max_length=-1)

    class Meta:
        managed = True
        db_table = 'ref_teaching_staff_selection_mode'


class RefUniversityCollegeType(models.Model):
    id = models.CharField(primary_key=True, max_length=-1)
    type = models.CharField(max_length=-1)

    class Meta:
        managed = True
        db_table = 'ref_university_college_type'


class RefUniversityType(models.Model):
    id = models.CharField(primary_key=True, max_length=-1)
    type = models.CharField(max_length=-1)

    class Meta:
        managed = True
        db_table = 'ref_university_type'


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
        managed = True
        db_table = 'ref_university'
        unique_together = (('id', 'survey_year'),)


class Accreditation(models.Model):
    id = models.IntegerField(primary_key=True)
    accreditation_body = models.CharField(max_length=-1)
    score = models.FloatField(blank=True, null=True)
    max_score = models.FloatField(blank=True, null=True)
    has_score = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'accreditation'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = True
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = True
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
        managed = True
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = True
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
        managed = True
        db_table = 'college'
        unique_together = (('id', 'survey_year'),)


class Department(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=-1)

    class Meta:
        managed = True
        db_table = 'department'


class Faculty(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=-1)

    class Meta:
        managed = True
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
        managed = True
        db_table = 'persons_count_by_category'


class Loan(models.Model):
    id = models.IntegerField(primary_key=True)
    count_by_category = models.ForeignKey('PersonsCountByCategory', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'loan'


class NonTeachingStaffCount(models.Model):
    id = models.IntegerField(primary_key=True)
    staff_type = models.ForeignKey('RefNonTeachingStaffType', models.DO_NOTHING)
    group = models.ForeignKey('RefNonTeachingStaffGroup', models.DO_NOTHING)
    sanctioned_strength = models.IntegerField()
    posts_reserved_for_pwd = models.IntegerField(blank=True, null=True)
    count_by_category = models.ForeignKey('PersonsCountByCategory', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'non_teaching_staff_count'


class PrivateStudentsResult(models.Model):
    id = models.IntegerField(primary_key=True)
    level = models.ForeignKey('RefCourseLevel', models.DO_NOTHING)
    programme = models.ForeignKey('RefProgramme', models.DO_NOTHING)
    broad_discipline_group_category = models.ForeignKey('RefBroadDisciplineGroupCategory', models.DO_NOTHING)
    broad_discipline_group = models.ForeignKey('RefBroadDisciplineGroup', models.DO_NOTHING)
    discipline = models.CharField(max_length=-1)
    appeared_total = models.IntegerField()
    appeared_female = models.IntegerField()
    passed_total = models.IntegerField()
    passed_female = models.IntegerField()
    first_class_passed_total = models.IntegerField()
    first_class_passed_female = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'private_students_result'


class StaffQuarter(models.Model):
    id = models.IntegerField(primary_key=True)
    non_teaching_staff = models.IntegerField(blank=True, null=True)
    teaching_staff = models.IntegerField(blank=True, null=True)
    total = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'staff_quarter'


class Course(models.Model):
    id = models.IntegerField(primary_key=True)
    mode = models.ForeignKey('RefCourseMode', models.DO_NOTHING, blank=True, null=True)
    only_through_colleges = models.BooleanField(blank=True, null=True)
    level = models.ForeignKey('RefCourseLevel', models.DO_NOTHING, blank=True, null=True)
    programme = models.ForeignKey('RefProgramme', models.DO_NOTHING, blank=True, null=True)
    discipline = models.CharField(max_length=-1, blank=True, null=True)
    broad_discipline_group = models.ForeignKey('RefBroadDisciplineGroup', models.DO_NOTHING, db_column='broad_discipline_group', blank=True, null=True)
    intake = models.IntegerField(blank=True, null=True)
    no_of_applicants = models.IntegerField(blank=True, null=True)
    duration_year = models.IntegerField(blank=True, null=True)
    duration_month = models.IntegerField(blank=True, null=True)
    type_id = models.IntegerField(blank=True, null=True)
    examination_system = models.ForeignKey('RefExaminationSystem', models.DO_NOTHING, blank=True, null=True)
    approving_statutory_body = models.ForeignKey('RefProgrammeStatutoryBody', models.DO_NOTHING, blank=True, null=True)
    approving_university = models.ForeignKey('RefUniversity', models.DO_NOTHING, blank=True, null=True)
    broad_discipline_group_category = models.ForeignKey('RefBroadDisciplineGroupCategory', models.DO_NOTHING, blank=True, null=True)
    admission_criterion_id = models.IntegerField(blank=True, null=True)
    survey_year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'course'


class Scholarship(models.Model):
    id = models.IntegerField(primary_key=True)
    count_by_category = models.ForeignKey(PersonsCountByCategory, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'scholarship'


class University(models.Model):
    aishe_code = models.CharField(max_length=-1)
    id = models.OneToOneField(RefUniversity, models.DO_NOTHING, db_column='id', primary_key=True)
    address_line1 = models.CharField(max_length=-1)
    address_line2 = models.CharField(max_length=-1, blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    city = models.CharField(max_length=-1, blank=True, null=True)
    constructed_area = models.FloatField(blank=True, null=True)
    district_code = models.CharField(max_length=-1)
    girl_exclusive = models.BooleanField()
    specialized = models.BooleanField()
    staff_quarter_available = models.BooleanField()
    student_hostel_available = models.BooleanField()
    location = models.CharField(max_length=-1)
    no_of_student_hostel = models.IntegerField()
    no_of_regional_centers = models.IntegerField()
    other_speciality = models.CharField(max_length=-1, blank=True, null=True)
    state_code = models.ForeignKey(RefDistrict, models.DO_NOTHING, db_column='state_code')
    website = models.CharField(max_length=-1, blank=True, null=True)
    year_of_establishment = models.IntegerField(blank=True, null=True)
    year_when_declared_university = models.IntegerField(blank=True, null=True)
    nodal_officer_id = models.IntegerField()
    staff_quarter = models.ForeignKey(StaffQuarter, models.DO_NOTHING, blank=True, null=True)
    type = models.ForeignKey(RefUniversityType, models.DO_NOTHING)
    offers_distance_programme = models.BooleanField()
    has_faculty_regular_courses = models.BooleanField()
    has_department_regular_courses = models.BooleanField()
    has_other_regular_courses = models.BooleanField()
    constituted_from_colleges = models.BooleanField()
    speciality = models.ForeignKey(RefSpeciality, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=-1)
    survey_year = models.IntegerField()
    financial_income_id = models.IntegerField()
    financial_expenditure_id = models.IntegerField()
    infrastructure_id = models.IntegerField()
    remarks = models.CharField(max_length=-1, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    scholarship = models.ForeignKey(Scholarship, models.DO_NOTHING, blank=True, null=True)
    loan = models.ForeignKey(Loan, models.DO_NOTHING, blank=True, null=True)
    offers_scholarship = models.BooleanField()
    offers_loan = models.BooleanField()
    is_accredited = models.BooleanField()
    is_foreign_students_enrolled = models.BooleanField()
    pin_code = models.IntegerField()
    off_shore_center_available = models.BooleanField()
    no_of_off_shore_center = models.IntegerField()
    has_fellowships = models.BooleanField()
    fellowships_id = models.IntegerField(blank=True, null=True)
    has_other_minority_data = models.BooleanField()
    block_city_town = models.CharField(max_length=-1, blank=True, null=True)
    is_university_uploaded_act_statues = models.BooleanField(blank=True, null=True)
    is_university_complying_rules = models.BooleanField(blank=True, null=True)
    is_university180_actual_teaching_days = models.BooleanField(blank=True, null=True)
    has_foreign_teachers = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'university'
        unique_together = (('id', 'survey_year'),)


class RegionalCenter(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=-1)
    university = models.ForeignKey('University', models.DO_NOTHING)
    no_of_study_centers = models.IntegerField(blank=True, null=True)
    district_code = models.CharField(max_length=-1)
    state_code = models.ForeignKey(RefDistrict, models.DO_NOTHING, db_column='state_code')
    survey_year = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'regional_center'


class UniversityAccreditation(models.Model):
    university = models.ForeignKey(University, models.DO_NOTHING)
    survey_year = models.IntegerField()
    accreditation = models.OneToOneField(Accreditation, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = True
        db_table = 'university_accreditation'


class UniversityDepartment(models.Model):
    university = models.ForeignKey(University, models.DO_NOTHING)
    department = models.OneToOneField(Department, models.DO_NOTHING, primary_key=True)
    survey_year = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'university_department'


class UniversityFaculty(models.Model):
    university = models.ForeignKey(University, models.DO_NOTHING)
    faculty = models.ForeignKey(Faculty, models.DO_NOTHING)
    survey_year = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'university_faculty'


class TeachingStaffSanctionedStrength(models.Model):
    id = models.IntegerField(primary_key=True)
    designation = models.ForeignKey(RefTeachingStaffDesignation, models.DO_NOTHING, blank=True, null=True)
    sanctioned_strength = models.IntegerField(blank=True, null=True)
    in_position = models.IntegerField(blank=True, null=True)
    in_position_direct = models.IntegerField(blank=True, null=True)
    in_position_cas = models.IntegerField(blank=True, null=True)
    no_of_phd_teachers = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'teaching_staff_sanctioned_strength'


class StudentHostel(models.Model):
    id = models.IntegerField(primary_key=True)
    intake_capacity = models.IntegerField()
    name = models.CharField(max_length=-1)
    students_residing = models.IntegerField()
    type = models.ForeignKey(RefStudentHostelType, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'student_hostel'


class TeachingStaff(models.Model):
    id = models.IntegerField(primary_key=True)
    faculty_name = models.CharField(max_length=-1, blank=True, null=True)
    department_name = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'teaching_staff'


class StandaloneInstitution(models.Model):
    aishe_code = models.CharField(max_length=-1)
    id = models.IntegerField(primary_key=True)
    address_line1 = models.CharField(max_length=-1, blank=True, null=True)
    address_line2 = models.CharField(max_length=-1, blank=True, null=True)
    city = models.CharField(max_length=-1, blank=True, null=True)
    state_code = models.ForeignKey(RefDistrict, models.DO_NOTHING, db_column='state_code', blank=True, null=True)
    district_code = models.CharField(max_length=-1, blank=True, null=True)
    website = models.CharField(max_length=-1, blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    constructed_area = models.FloatField(blank=True, null=True)
    year_of_establishment = models.IntegerField(blank=True, null=True)
    year_of_recognition = models.IntegerField(blank=True, null=True)
    nodalofficer_id = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=-1, blank=True, null=True)
    awards_degree_through_university = models.BooleanField(blank=True, null=True)
    university_id = models.CharField(max_length=-1, blank=True, null=True)
    girl_exclusive = models.BooleanField(blank=True, null=True)
    staff_quarter_available = models.BooleanField(blank=True, null=True)
    staff_quarter_id = models.IntegerField(blank=True, null=True)
    student_hostel_available = models.BooleanField(blank=True, null=True)
    no_of_student_hostel = models.IntegerField(blank=True, null=True)
    management = models.ForeignKey(RefInstitutionManagement, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    survey_year = models.IntegerField()
    financial_income_id = models.IntegerField(blank=True, null=True)
    financial_expenditure_id = models.IntegerField(blank=True, null=True)
    infrastructure_id = models.IntegerField(blank=True, null=True)
    remarks = models.CharField(max_length=-1, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    scholarship = models.ForeignKey(Scholarship, models.DO_NOTHING, blank=True, null=True)
    loan = models.ForeignKey(Loan, models.DO_NOTHING, blank=True, null=True)
    is_accredited = models.BooleanField(blank=True, null=True)
    is_foreign_students_enrolled = models.BooleanField(blank=True, null=True)
    offers_scholarship = models.BooleanField(blank=True, null=True)
    offers_loan = models.BooleanField(blank=True, null=True)
    offers_distance_programme = models.BooleanField(blank=True, null=True)
    pin_code = models.IntegerField(blank=True, null=True)
    has_fellowships = models.BooleanField(blank=True, null=True)
    fellowships_id = models.IntegerField(blank=True, null=True)
    ministry_id = models.IntegerField(blank=True, null=True)
    has_other_minority_data = models.BooleanField(blank=True, null=True)
    block_city_town = models.CharField(max_length=-1, blank=True, null=True)
    has_foreign_teachers = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'standalone_institution'
        unique_together = (('id', 'survey_year'),)


class UniversityPrivateStudentsResult(models.Model):
    university = models.ForeignKey(University, models.DO_NOTHING)
    survey_year = models.IntegerField()
    private_students_result = models.ForeignKey(PrivateStudentsResult, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'university_private_students_result'


class UniversityStudentHostel(models.Model):
    university = models.ForeignKey(University, models.DO_NOTHING)
    student_hostel = models.ForeignKey(StudentHostel, models.DO_NOTHING)
    survey_year = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'university_student_hostel'


class StandaloneInstitutionStudentHostel(models.Model):
    standalone_institution = models.ForeignKey(StandaloneInstitution, models.DO_NOTHING)
    student_hostel = models.ForeignKey('StudentHostel', models.DO_NOTHING)
    survey_year = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'standalone_institution_student_hostel'


class StandaloneInstitutionTeachingStaff(models.Model):
    standalone_institution = models.ForeignKey(StandaloneInstitution, models.DO_NOTHING)
    survey_year = models.IntegerField()
    teaching_staff = models.ForeignKey('TeachingStaff', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'standalone_institution_teaching_staff'


class StandaloneInstitutionTeachingStaffSanctionedStrength(models.Model):
    standalone_institution = models.ForeignKey(StandaloneInstitution, models.DO_NOTHING)
    survey_year = models.IntegerField()
    teaching_staff_sanctioned_strength = models.ForeignKey('TeachingStaffSanctionedStrength', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'standalone_institution_teaching_staff_sanctioned_strength'


class TeachingStaffCount(models.Model):
    id = models.IntegerField(primary_key=True)
    teaching_staff = models.ForeignKey(TeachingStaff, models.DO_NOTHING, blank=True, null=True)
    designation = models.ForeignKey(RefTeachingStaffDesignation, models.DO_NOTHING, blank=True, null=True)
    grade_pay = models.CharField(max_length=-1, blank=True, null=True)
    selection_mode = models.ForeignKey(RefTeachingStaffSelectionMode, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'teaching_staff_count'


class UniversityTeachingStaff(models.Model):
    university = models.ForeignKey(University, models.DO_NOTHING)
    survey_year = models.IntegerField()
    teaching_staff = models.ForeignKey(TeachingStaff, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'university_teaching_staff'


class UniversityTeachingStaffSanctionedStrength(models.Model):
    university = models.ForeignKey(University, models.DO_NOTHING)
    survey_year = models.IntegerField()
    teaching_staff_sanctioned_strength = models.ForeignKey(TeachingStaffSanctionedStrength, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'university_teaching_staff_sanctioned_strength'


class StandaloneInstitutionAccreditation(models.Model):
    standalone_institution = models.ForeignKey(StandaloneInstitution, models.DO_NOTHING)
    survey_year = models.IntegerField()
    accreditation = models.ForeignKey(Accreditation, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'standalone_institution_accreditation'


class StandaloneInstitutionDepartment(models.Model):
    standalone_institution = models.ForeignKey(StandaloneInstitution, models.DO_NOTHING)
    department = models.ForeignKey(Department, models.DO_NOTHING)
    survey_year = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'standalone_institution_department'


class StandaloneInstitutionFaculty(models.Model):
    standalone_institution = models.ForeignKey(StandaloneInstitution, models.DO_NOTHING)
    faculty = models.ForeignKey(Faculty, models.DO_NOTHING)
    survey_year = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'standalone_institution_faculty'


class Infrastructure(models.Model):
    id = models.IntegerField(primary_key=True)
    playground = models.BooleanField(blank=True, null=True)
    auditorium = models.BooleanField(blank=True, null=True)
    theatre = models.BooleanField(blank=True, null=True)
    library = models.BooleanField(blank=True, null=True)
    laboratory = models.BooleanField(blank=True, null=True)
    conference_hall = models.BooleanField(blank=True, null=True)
    health_center = models.BooleanField(blank=True, null=True)
    gymnasium_fitness_center = models.BooleanField(blank=True, null=True)
    indoor_stadium = models.BooleanField(blank=True, null=True)
    common_room = models.BooleanField(blank=True, null=True)
    computer_center = models.BooleanField(blank=True, null=True)
    cafeteria = models.BooleanField(blank=True, null=True)
    guest_house = models.BooleanField(blank=True, null=True)
    no_of_playgrounds = models.IntegerField(blank=True, null=True)
    no_of_auditoriums = models.IntegerField(blank=True, null=True)
    no_of_theatres = models.IntegerField(blank=True, null=True)
    no_of_libraries = models.IntegerField(blank=True, null=True)
    no_of_laboratories = models.IntegerField(blank=True, null=True)
    no_of_conference_halls = models.IntegerField(blank=True, null=True)
    no_of_health_centers = models.IntegerField(blank=True, null=True)
    no_of_gymnasim_fitness_centers = models.IntegerField(blank=True, null=True)
    no_of_indoor_stadiums = models.IntegerField(blank=True, null=True)
    no_of_common_rooms = models.IntegerField(blank=True, null=True)
    no_of_computer_centers = models.IntegerField(blank=True, null=True)
    no_of_cafeteria = models.IntegerField(blank=True, null=True)
    no_of_guest_houses = models.IntegerField(blank=True, null=True)
    separate_room_for_girls = models.BooleanField(blank=True, null=True)
    no_of_separate_rooms_for_girls = models.IntegerField(blank=True, null=True)
    solar_power_generation = models.BooleanField(blank=True, null=True)
    connectivity_nkn = models.BooleanField(blank=True, null=True)
    connectivity_nmeict = models.BooleanField(blank=True, null=True)
    no_of_books = models.IntegerField(blank=True, null=True)
    no_of_journals = models.IntegerField(blank=True, null=True)
    campus_friendly = models.BooleanField(blank=True, null=True)
    grievance_redressal_mechanism = models.BooleanField(blank=True, null=True)
    vigilance_cell = models.BooleanField(blank=True, null=True)
    opportunity_cell = models.BooleanField(blank=True, null=True)
    separate_toilet_for_disabled_female = models.BooleanField(blank=True, null=True)
    ramp_attached_to_classroom_library = models.BooleanField(blank=True, null=True)
    sexual_harassment_cell = models.BooleanField(blank=True, null=True)
    counselors_for_students = models.BooleanField(blank=True, null=True)
    clinic_first_aid_room = models.BooleanField(blank=True, null=True)
    separate_toilet_for_girls = models.BooleanField(blank=True, null=True)
    skill_development_centre = models.BooleanField(blank=True, null=True)
    self_defence_class_for_females = models.BooleanField(blank=True, null=True)
    institution_disaster_management_facilities = models.BooleanField(blank=True, null=True)
    capacity_building_and_training_aware_programme_conducted = models.BooleanField(blank=True, null=True)
    vulnerability_assess_checks_made_during_year = models.BooleanField(blank=True, null=True)
    any_mock_drill_rehearsal_programme_conducted = models.BooleanField(blank=True, null=True)
    anti_ragging_cell = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'infrastructure'


class EnrolledForeignStudentCount(models.Model):
    id = models.IntegerField(primary_key=True)
    country = models.ForeignKey('RefCountry', models.DO_NOTHING)
    programme = models.ForeignKey('RefProgramme', models.DO_NOTHING)
    discipline = models.CharField(max_length=-1)
    total = models.IntegerField()
    girls = models.IntegerField()
    broad_discipline_group = models.ForeignKey('RefBroadDisciplineGroup', models.DO_NOTHING)
    level = models.ForeignKey('RefCourseLevel', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'enrolled_foreign_student_count'


class EnrolledStudentCount(models.Model):
    id = models.IntegerField(primary_key=True)
    course_mode = models.ForeignKey('RefCourseMode', models.DO_NOTHING, blank=True, null=True)
    level = models.ForeignKey('RefCourseLevel', models.DO_NOTHING, blank=True, null=True)
    programme = models.ForeignKey('RefProgramme', models.DO_NOTHING, blank=True, null=True)
    discipline = models.CharField(max_length=-1, blank=True, null=True)
    course_type = models.ForeignKey('RefCourseType', models.DO_NOTHING, blank=True, null=True)
    year = models.CharField(max_length=-1, blank=True, null=True)
    count_by_category = models.ForeignKey('PersonsCountByCategory', models.DO_NOTHING, blank=True, null=True)
    broad_discipline_group = models.ForeignKey('RefBroadDisciplineGroup', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'enrolled_student_count'


class ExaminationResult(models.Model):
    id = models.IntegerField(primary_key=True)
    course_mode = models.ForeignKey('RefCourseMode', models.DO_NOTHING, blank=True, null=True)
    course_level = models.ForeignKey('RefCourseLevel', models.DO_NOTHING, blank=True, null=True)
    programme = models.ForeignKey('RefProgramme', models.DO_NOTHING, blank=True, null=True)
    discipline = models.CharField(max_length=-1, blank=True, null=True)
    appeared_total = models.IntegerField(blank=True, null=True)
    appeared_female = models.IntegerField(blank=True, null=True)
    passed_total = models.IntegerField(blank=True, null=True)
    passed_female = models.IntegerField(blank=True, null=True)
    broad_discipline_group_id = models.CharField(max_length=-1, blank=True, null=True)
    first_class_passed_total = models.IntegerField(blank=True, null=True)
    first_class_passed_female = models.IntegerField(blank=True, null=True)
    course_id = models.IntegerField(blank=True, null=True)
    examination_result_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'examination_result'


class FacultyDepartment(models.Model):
    faculty = models.ForeignKey(Faculty, models.DO_NOTHING)
    department = models.ForeignKey(Department, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'faculty_department'


class UniversityNonTeachingStaffCount(models.Model):
    university = models.ForeignKey(University, models.DO_NOTHING)
    survey_year = models.IntegerField()
    non_teaching_staff_count = models.ForeignKey(NonTeachingStaffCount, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'university_non_teaching_staff_count'


class EnrolledDistanceStudentUniversity(models.Model):
    id = models.IntegerField(primary_key=True)
    regional_center_name = models.CharField(max_length=-1)
    state_code = models.ForeignKey('RefDistrict', models.DO_NOTHING, db_column='state_code')
    district_code = models.CharField(max_length=-1)

    class Meta:
        managed = True
        db_table = 'enrolled_distance_student_university'


class StandaloneInstitutionNonTeachingStaffCount(models.Model):
    standalone_institution = models.ForeignKey(StandaloneInstitution, models.DO_NOTHING)
    survey_year = models.IntegerField()
    non_teaching_staff_count = models.ForeignKey(NonTeachingStaffCount, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'standalone_institution_non_teaching_staff_count'


class CollegeInstitution(models.Model):
    aishe_code = models.CharField(max_length=-1)
    id = models.OneToOneField(College, models.DO_NOTHING, db_column='id', primary_key=True)
    address_line1 = models.CharField(max_length=-1)
    address_line2 = models.CharField(max_length=-1, blank=True, null=True)
    city = models.CharField(max_length=-1, blank=True, null=True)
    state_code = models.ForeignKey('RefDistrict', models.DO_NOTHING, db_column='state_code')
    district_code = models.CharField(max_length=-1)
    website = models.CharField(max_length=-1, blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    constructed_area = models.FloatField(blank=True, null=True)
    year_of_establishment = models.IntegerField(blank=True, null=True)
    nodalofficer_id = models.IntegerField()
    university_id = models.CharField(max_length=-1)
    statutory_body_id = models.CharField(max_length=-1, blank=True, null=True)
    other_statutory_body = models.CharField(max_length=-1, blank=True, null=True)
    year_of_affiliation = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=-1)
    autonomous = models.BooleanField()
    management = models.ForeignKey('RefInstitutionManagement', models.DO_NOTHING)
    specialized = models.BooleanField()
    other_speciality = models.CharField(max_length=-1, blank=True, null=True)
    evening = models.BooleanField()
    girl_exclusive = models.BooleanField()
    staff_quarter_available = models.BooleanField()
    staff_quarter_id = models.IntegerField(blank=True, null=True)
    student_hostel_available = models.BooleanField()
    no_of_student_hostel = models.IntegerField()
    speciality = models.ForeignKey('RefSpeciality', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=-1)
    survey_year = models.IntegerField()
    financial_income_id = models.IntegerField()
    financial_expenditure_id = models.IntegerField()
    infrastructure = models.ForeignKey('Infrastructure', models.DO_NOTHING)
    remarks = models.CharField(max_length=-1, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    scholarship = models.ForeignKey('Scholarship', models.DO_NOTHING, blank=True, null=True)
    loan = models.ForeignKey('Loan', models.DO_NOTHING, blank=True, null=True)
    is_accredited = models.BooleanField()
    is_foreign_students_enrolled = models.BooleanField()
    offers_scholarship = models.BooleanField()
    offers_loan = models.BooleanField()
    has_diploma_courses = models.BooleanField()
    diploma_course = models.ForeignKey('RefDiplomaCourse', models.DO_NOTHING, blank=True, null=True)
    college_type = models.ForeignKey('RefUniversityCollegeType', models.DO_NOTHING)
    pin_code = models.IntegerField(blank=True, null=True)
    has_fellowships = models.BooleanField()
    fellowships_id = models.IntegerField(blank=True, null=True)
    other_affiliated_university_id = models.CharField(max_length=-1, blank=True, null=True)
    has_other_minority_data = models.BooleanField()
    block_city_town = models.CharField(max_length=-1, blank=True, null=True)
    has_foreign_teachers = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'college_institution'
        unique_together = (('id', 'survey_year'),)


class CollegeInstitutionAccreditation(models.Model):
    college_institution = models.ForeignKey(CollegeInstitution, models.DO_NOTHING)
    survey_year = models.IntegerField()
    accreditation = models.OneToOneField(Accreditation, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = True
        db_table = 'college_institution_accreditation'


class CollegeInstitutionDepartment(models.Model):
    college_institution = models.ForeignKey(CollegeInstitution, models.DO_NOTHING)
    department = models.OneToOneField('Department', models.DO_NOTHING, primary_key=True)
    survey_year = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'college_institution_department'


class CollegeInstitutionNonTeachingStaffCount(models.Model):
    college_institution = models.ForeignKey(CollegeInstitution, models.DO_NOTHING)
    survey_year = models.IntegerField()
    non_teaching_staff_count = models.OneToOneField('NonTeachingStaffCount', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = True
        db_table = 'college_institution_non_teaching_staff_count'


class CollegeInstitutionStudentHostel(models.Model):
    college_institution = models.ForeignKey(CollegeInstitution, models.DO_NOTHING)
    student_hostel = models.ForeignKey('StudentHostel', models.DO_NOTHING)
    survey_year = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'college_institution_student_hostel'


class CollegeInstitutionTeachingStaff(models.Model):
    college_institution = models.ForeignKey(CollegeInstitution, models.DO_NOTHING)
    survey_year = models.IntegerField()
    teaching_staff = models.ForeignKey('TeachingStaff', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'college_institution_teaching_staff'


class EnrolledDistanceStudentUniversityCount(models.Model):
    enrolled_distance_student_university = models.ForeignKey(EnrolledDistanceStudentUniversity, models.DO_NOTHING)
    enrolled_student_count_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'enrolled_distance_student_university_count'


class CourseExaminationResult(models.Model):
    id = models.IntegerField(primary_key=True)
    course = models.ForeignKey(Course, models.DO_NOTHING, blank=True, null=True)
    examination_result = models.ForeignKey('ExaminationResult', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'course_examination_result'


class CourseEnrolledForeignStudentCount(models.Model):
    id = models.IntegerField(primary_key=True)
    course = models.ForeignKey(Course, models.DO_NOTHING)
    enrolled_foreign_student_count = models.ForeignKey('EnrolledForeignStudentCount', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'course_enrolled_foreign_student_count'


class CourseEnrolledStudentCount(models.Model):
    id = models.IntegerField(primary_key=True)
    course = models.ForeignKey(Course, models.DO_NOTHING, blank=True, null=True)
    enrolled_student_count = models.ForeignKey('EnrolledStudentCount', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'course_enrolled_student_count'


class UniversityEnrolledDistanceStudent(models.Model):
    university = models.ForeignKey(University, models.DO_NOTHING)
    survey_year = models.IntegerField()
    enrolled_distance_student_university = models.ForeignKey(EnrolledDistanceStudentUniversity, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'university_enrolled_distance_student'


class EducationalInstitutionCourse(models.Model):
    institution_category = models.CharField(max_length=-1)
    institution = models.ForeignKey(CollegeInstitution, models.DO_NOTHING)
    state_code = models.ForeignKey('RefState', models.DO_NOTHING, db_column='state_code', blank=True, null=True)
    faculty = models.ForeignKey('Faculty', models.DO_NOTHING, blank=True, null=True)
    department = models.ForeignKey(Department, models.DO_NOTHING, blank=True, null=True)
    course = models.ForeignKey(Course, models.DO_NOTHING, blank=True, null=True)
    survey_year = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'educational_institution_course'


class CollegeInstitutionTeachingStaffSanctionedStrength(models.Model):
    college_institution = models.ForeignKey(CollegeInstitution, models.DO_NOTHING)
    survey_year = models.IntegerField()
    teaching_staff_sanctioned_strength = models.ForeignKey('TeachingStaffSanctionedStrength', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'college_institution_teaching_staff_sanctioned_strength'


class CollegeInstitutionFaculty(models.Model):
    college_institution = models.ForeignKey(CollegeInstitution, models.DO_NOTHING, blank=True, null=True)
    faculty = models.ForeignKey('Faculty', models.DO_NOTHING, blank=True, null=True)
    survey_year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'college_institution_faculty'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_session'








