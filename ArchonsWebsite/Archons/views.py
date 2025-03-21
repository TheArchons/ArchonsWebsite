from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect


def display(request, event=None):
    links = {
        '/': 'ArchonsWebsite/index.html',
        '/socials/': 'ArchonsWebsite/socials.html',
        '/projects/': 'ArchonsWebsite/projects.html',
        '/projects/': 'ArchonsWebsite/projects.html',
        '/whoami/': 'ArchonsWebsite/whoami.html'
    }

    if '/whoami' in request.path and event is not None:
        return render(request, f'ArchonsWebsite/whoami/{event}.html')

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


def yearbook(request):
    # log ip to a file
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    with open("ArchonsWebsite/ips.txt", "a") as f:
        f.write(ip + "\n")

    redirect_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ?autoplay=1"
    return redirect(redirect_url)


def robots(request):
    return render(request, 'ArchonsWebsite/robots.txt', content_type='text/plain')

def robot_test(request):
    # log ip to a file
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    with open("ArchonsWebsite/ips.txt", "a") as f:
        f.write(ip + "\n")
    
    redirect_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ?autoplay=1"
    return redirect(redirect_url)