from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.EmailField()
    mobile=models.CharField(max_length=200)
    message=models.TextField()
    def __str__(self):
        return self.first_name


class StudentCorner(models.Model):
    Gender=(
        ("Male","Male"),
        ("Female","Female"),
        ("Other","Other")
    )
    Fee_plan=(
        ("Lumpsum","Lumpsum"),
        ("Installments","Installments"),
        )
    Interested_Programme=(
        ("Python","Python"),
        ("Java","Java"),
        ("Android","Android"),
        ("Digital Marketing","Digital Marketing"),
        ("Personality Development","Personality Development"),
        ("Spoken English","Spoken English"),

    )
    Currently_Working=(
        ("Yes","Yes"),
        ("No","No"),
    )
    student_name=models.CharField(max_length=100)
    student_email=models.EmailField()
    student_mobile=models.CharField(max_length=100)
    student_dob=models.DateField()
    student_address=models.CharField(max_length=300)
    student_gender=models.CharField(choices=Gender,max_length=100)
    student_qualification=models.CharField(max_length=300)
    student_college=models.CharField(max_length=300)
    student_academic_marks=models.CharField(max_length=300)
    student_selected_language=models.CharField(max_length=200, choices=Interested_Programme)
    student_fee_plan=models.CharField(choices=Fee_plan, max_length=100)
    student_currently_working=models.CharField(choices=Currently_Working,  null=True,  max_length=10)
    student_current_organization=models.CharField(max_length=50, null=True, blank=True)
    student_total_experience=models.CharField(max_length=50, blank=True, null=True)
    student_designation=models.CharField(max_length=50, blank=True, null=True)
    student_upload_resume=models.ImageField(upload_to="images/", null=True, blank=True)

    def __str__(self):
        return self.student_name




class HrCorner(models.Model):
    Job_Experience=(
        ("Experienced","Experienced"),
          ("Fresher","Fresher"),

    )
    Communication_Skill=(
        ("Excellent","Excellent"),
        ("Good","Good",),
        ("Average","Average"),
    )
    Yes_No=(
        ("Yes","Yes"),
        ("No","No"),

    )
    Work_Environment=(
        ("24*7","24*7"),
         ("Day Shift","Day Shift"),
          ("Sat-Sun Fixed Weekly-offs","Sat-Sun Fixed Weekly-offs"),
           ("Rotational Offs","Rotational Offs"),

    )
    Project=(
        ("Voice","Voice"),
        ("Non-Voice","Non-Voice"),
        ("Technical","Technical"),
        ("Non-Technical","Non-Technical"),
    )
    email=models.EmailField()
    company=models.CharField(max_length=300)
    contact_person=models.CharField(max_length=300)
    designation=models.CharField(max_length=100)
    contact_number=models.CharField(max_length=100)
    company_website=models.CharField(max_length=200)
    company_registered_address=models.CharField(max_length=300)
    total_requirements=models.IntegerField()
    qualification_required=models.CharField(max_length=300)
    job_experience=models.CharField(max_length=100,choices=Job_Experience)
    communication_skill=models.CharField(max_length=100,choices=Communication_Skill)
    annual_salary=models.CharField(max_length=200)
    cab_facility=models.CharField(max_length=10, choices=Yes_No)
    incentive_plans=models.CharField(max_length=10, choices=Yes_No)
    interview_process=models.CharField(max_length=10, choices=Yes_No)
    group_discussion=models.CharField(max_length=10, choices=Yes_No)
    hr_round=models.CharField(max_length=10,choices=Yes_No)
    technical_round=models.CharField(max_length=10, choices=Yes_No)
    work_environment=models.CharField(max_length=100,choices=Work_Environment)
    project=models.CharField(max_length=100,choices=Project)
    hiring_position=models.CharField(max_length=100)
    major_responsibities=models.CharField(max_length=500)

    def __str__(self):
        return self.company


class AskQuery(models.Model):
    user_email=models.EmailField()

    def __str__(self):
        return self.user_email


class SoftwareDevelopment(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    contact=models.CharField(max_length=20)
    skype_id=models.CharField(max_length=100)
    project_details=models.CharField(max_length=200)

    def __str__(self):
        return self.name