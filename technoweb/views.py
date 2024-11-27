from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import *
from django.contrib import messages

def index(request):
    return render(request,'index.html',{})

def home(request):
    return render(request,'home.html',{})

def education(request):
    return render(request,'education.html')

def english_pdp(request):
    return render(request, 'english_pdp.html')



def services(request):
    return render(request,'services.html')


def contact(request):
    if request.method=="POST":
        f_name=request.POST.get('first_name')
        l_name=request.POST.get('last_name')
        user_email=request.POST.get('email')
        user_contact=request.POST.get('contact')
        user_message=request.POST.get('message')
        con=Contact()
        con.first_name=f_name
        con.last_name=l_name
        con.email=user_email
        con.mobile=user_contact
        con.message=user_message
        con.save()
        success_msg = "Form Submitted Successfully!!"

        
    return render(request,'home.html', {'success_msg':success_msg})

def studentCorner(request):
    if request.method=="POST":
        register_name=request.POST.get('register_name')
        register_email=request.POST.get('register_email')
        register_mobile=request.POST.get('register_mobile')
        register_dob=request.POST.get('register_dob')
        register_address=request.POST.get('register_address')
        register_location=request.POST.get('register_location')
        register_gender=request.POST.get('register_gender')
        register_college=request.POST.get('register_college')
        register_qualification=request.POST.get('register_qualification')
        register_academic_marks=request.POST.get('register_academic_marks')
        registered_programming_language=request.POST.get('registered_programming_language')
        register_fee_plan=request.POST.get('register_fee_plan')
        register_currently_working=request.POST.get('register_currently_working')
        register_current_organization=request.POST.get('register_current_organization')
        register_total_experience=request.POST.get('register_total_experience')
        register_designation=request.POST.get('register_designation')
        register_resume=request.FILES.get('register_resume')

        student_corner=StudentCorner()
        student_corner.student_name=register_name
        student_corner.student_email=register_email
        student_corner.student_mobile=register_mobile
        student_corner.student_dob=register_dob
        student_corner.student_address=register_address
        student_corner.register_location=register_location
        student_corner.student_gender=register_gender
        student_corner.student_qualification=register_qualification
        student_corner.student_college=register_college
        student_corner.student_academic_marks=register_academic_marks
        student_corner.student_selected_language=registered_programming_language
        student_corner.student_fee_plan=register_fee_plan
        student_corner.student_currently_working=register_currently_working
        student_corner.student_current_organization=register_current_organization
        student_corner.student_total_experience=register_total_experience
        student_corner.student_designation=register_designation
        student_corner.student_upload_resume=register_resume
        student_corner.save()
        
        success_msg = "Form Submitted Successfully!!"
        return render(request,'registration_form.html', {'success_msg':success_msg})
    return render(request,'registration_form.html')



def hrCorner(request):
    if request.method=="POST":
        hr_email=request.POST.get('hr_email')
        hr_company_name=request.POST.get('hr_company_name')
        hr_contact_person=request.POST.get('hr_contact_person')
        hr_designation=request.POST.get('hr_designation')
        hr_contact=request.POST.get('hr_contact')
        hr_website=request.POST.get('hr_website')
        hr_company_registered_address=request.POST.get('hr_company_registered_address')
        hr_total_requirements=request.POST.get('hr_total_requirements')
        hr_qualification_required=request.POST.get('hr_qualification_required')
        job_experience=request.POST.get('job_experience')

        communication_skill=request.POST.get('communication_skill')
        hr_annual_salary=request.POST.get('hr_annual_salary')
        cab_facility=request.POST.get('cab_facility')
        incentive_plans=request.POST.get('incentive_plans')
        interview_process=request.POST.get('interview_process')

        group_discussion=request.POST.get('group_discussion')
        hr_round=request.POST.get('hr_round')
        technical_round=request.POST.get('technical_round')

        work_environment=request.POST.get('work_environment')
        project=request.POST.get('project')
        hr_hiring_position=request.POST.get('hr_hiring_position')
        hr_major_responsibity=request.POST.get('hr_major_responsibity')
        hr_corner=HrCorner()
        hr_corner.email=hr_email
        hr_corner.company=hr_company_name
        hr_corner.contact_person=hr_contact_person
        hr_corner.designation=hr_designation
        hr_corner.contact_number=hr_contact
        hr_corner.company_website=hr_website
        hr_corner.company_registered_address=hr_company_registered_address
        hr_corner.total_requirements=hr_total_requirements
        hr_corner.qualification_required=hr_qualification_required
        hr_corner.job_experience=job_experience
        hr_corner.communication_skill=communication_skill
        hr_corner.annual_salary=hr_annual_salary
        hr_corner.cab_facility=cab_facility
        hr_corner.incentive_plans=incentive_plans
        hr_corner.interview_process=interview_process
        hr_corner.group_discussion=group_discussion
        hr_corner.hr_round=hr_round
        hr_corner.technical_round=technical_round
        hr_corner.work_environment=work_environment
        hr_corner.project=project
        hr_corner.hiring_position=hr_hiring_position
        hr_corner.major_responsibities=hr_major_responsibity
        hr_corner.save()
        success_msg = "Form Submitted Successfully!!"
        return render(request,'hr_register_form.html', {'success_msg':success_msg})
    return render(request,'hr_register_form.html')


def askQuery(request):
    if request.method=="POST":
        footer_email=request.POST.get('footer_email')
        ask_query=AskQuery()
        ask_query.user_email=footer_email
        ask_query.save()
        return render(request,'index.html')
    return render(request,'index.html')


def softwareDevelopment(request):
    if request.method=="POST":

        name=request.POST.get('name')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        skype_id=request.POST.get('skype_id')
        project_details=request.POST.get('project_detail')

        software_dev=SoftwareDevelopment()
        software_dev.name=name
        software_dev.email=email
        software_dev.contact=contact
        software_dev.skype_id=skype_id
        software_dev.project_details=project_details
        software_dev.save()
        return render(request,'software_development.html')
    return render(request,'software_development.html')
