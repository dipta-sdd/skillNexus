from django.urls import path

from . import views

urlpatterns = [
    path('signup', views.signup),
    path('login', views.login_view),
    path('current_user', views.current_user),
    path('edit_profile', views.editProfile),
    path('personal_details', views.getPersonaDetails),
    path('personal_details/edit', views.editPersonaDetails),

    # educal api

    path('edu', views.edu_get),
    path('edu/level', views.edu_level),
    path('edu/degree', views.edu_degree),
    path('edu/group_or_mejor', views.edu_group_or_mejor),
    path('education/add', views.addEducation),
    path('education/get', views.getEducation),
    path('education/del', views.delEducation),
    path('training/get', views.getTraining),
    path('training/del', views.delTraining),
    path('training/add', views.addTraining),
    path('experience/add', views.addExperience),
    path('experience/del', views.delExperience),
    path('experience/get', views.getExperience),
    path('employer/company/get', views.getCompany),
    path('employer/company/add', views.addCompany),
    path('university/get', views.getUniversity),
    path('university/add', views.addUniversity),
    path('university/program/add', views.addProgram),
    path('university/program/get', views.getProgram),
    path('university/program/del', views.deelProgram),
    path('program', views.getProgramStudent),
    path('skills/all', views.allSkill),
    path('skills/add', views.addSkill),
    path('skills/get', views.getSkill),
    path('skills/del', views.delSkill),

    path('course/add', views.addCourse),
    path('course/enroll', views.enroll_course),
    path('course_lecture/add', views.addCourseLecture),
    path('course/get', views.getCourseDetail),
    path('course_list_single/get', views.getSingleCourseDetail),
    path('course_del/del', views.delCourse),
    path('course_video/get', views.getCourseVideo),
    path('course_video/edit', views.edit_course_video),
    path('course/edit', views.editCourse),
    path('course_list/get', views.courselist),



    path('lecture/get', views.get_lectures, name='get_lectures'),

]
