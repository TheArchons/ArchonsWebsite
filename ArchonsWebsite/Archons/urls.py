from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('robots.txt', views.robots, name='robots'),
    path('socials/', views.socials, name='socials'),
    path('projects/', views.projects, name='projects'),
    path('projects/ArchonsWebsite/', views.projectsClass.ArchonsWebsite, name='socials_ArchonsWebsite'),
    path('projects/cs11FinalProject/', views.projectsClass.cs11FinalProject, name='socials_cs11FinalProject'),
]