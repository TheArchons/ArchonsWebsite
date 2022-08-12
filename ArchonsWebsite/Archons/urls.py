from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('robots.txt', views.robots, name='robots'),
    path('socials/', views.socials, name='socials'),
    path('whoami/', views.whoami, name='whoami'),

    path('projects/', views.projects, name='projects'),
    path('projects/winlauncher/', views.projectsClass.winLauncher, name='winlauncher'),
    path('projects/ArchonsWebsite/', views.projectsClass.ArchonsWebsite, name='socials_ArchonsWebsite'),
    path('projects/cs11FinalProject/', views.projectsClass.cs11FinalProject, name='socials_cs11FinalProject'),
    path('projects/FileTransfer/', views.projectsClass.FileTransfer, name='socials_FileTransfer'),
    path('projects/ISO8601ifier/', views.projectsClass.ISO8601ifier, name='socials_ISO8601ifier'),
    path('projects/Crinlist/', views.projectsClass.crinList, name='socials_crinList'),
    path('projects/yato/', views.projectsClass.yato, name='socials_yato'),
    path('projects/leetCode/', views.projectsClass.leetCode, name='socials_leetCode'),
    path('projects/WaterlooCCC/', views.projectsClass.WaterlooCCC, name='socials_WaterlooCCC'),
]