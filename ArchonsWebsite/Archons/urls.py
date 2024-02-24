from django.urls import path

from . import views

urlpatterns = [
    path('', views.display, name='index'),
    path('socials/', views.display),
    path('whoami/', views.display),

    path('projects/', views.display, name='projects'),
    path('projects/winlauncher/', views.projectsDisplay),
    path('projects/ArchonsWebsite/', views.projectsDisplay),
    path('projects/cs11FinalProject/', views.projectsDisplay),
    path('projects/FileTransfer/', views.projectsDisplay),
    path('projects/ISO8601ifier/', views.projectsDisplay),
    path('projects/Crinlist/', views.projectsDisplay),
    path('projects/yato/', views.projectsDisplay),
    path('projects/leetCode/', views.projectsDisplay),
    path('projects/CompetitiveProgramming/', views.projectsDisplay),

    path('yrbook/', views.yearbook),
    path('robot_test/', views.robot_test),

    path('robots.txt', views.robots)
]