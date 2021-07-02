from django.urls import path
from . import views

urlpatterns = [   
    path('skills/', views.getSkills, name="skills"),
    path('projects/', views.getProjects, name="Projects"),
    path('languages/', views.getLanguages, name="Languages"),
    path('tools/', views.getTools, name="Tools"),
]