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
]
