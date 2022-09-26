from django.shortcuts import render
from django.conf import settings


def display(request):
    links = {
        '/': 'ArchonsWebsite/index.html',
        '/socials/': 'ArchonsWebsite/socials.html',
        '/projects/': 'ArchonsWebsite/projects.html',
        '/projects/': 'ArchonsWebsite/projects.html',
    }
    return render(request, links[request.path])


def projectsDisplay(request):
    links = {
        '/winlauncher/': 'ArchonsWebsite/projects/winlauncher.html',
        '/ArchonsWebsite/': 'ArchonsWebsite/projects/ArchonsWebsite.html',
        '/cs11FinalProject/': 'ArchonsWebsite/projects/cs11FinalProject.html',
        '/FileTransfer/': 'ArchonsWebsite/projects/FileTransfer.html',
        '/ISO8601ifier/': 'ArchonsWebsite/projects/ISO8601ifier.html',
        '/Crinlist/': 'ArchonsWebsite/projects/crinList.html',
        '/yato/': 'ArchonsWebsite/projects/yato.html',
        '/leetCode/': 'ArchonsWebsite/projects/leetcode.html',
        '/CompetitiveProgramming/': 'ArchonsWebsite/projects/CompetitiveProgramming.html',
    }

    # 9 is the length of '/projects'
    return render(request, links[request.path[9:]])
