from django.urls import path
from technoweb import views


# from . import views


urlpatterns=[
  
    path('', views.home, name="home"),
    path('placements', views.services, name="services"),
    path('education',views.education, name="education"),
    path('english_pdp',views.english_pdp, name="english_pdp"),
    path('contact',views.contact,name='contact'),
    path('student_corner', views.studentCorner, name="student_corner"),
    path('hr_corner', views.hrCorner,name="hr_corner"),
    path('ask_query',views.askQuery,name="ask_query"),
    path('software_development', views.softwareDevelopment, name="software_development"),
    

]