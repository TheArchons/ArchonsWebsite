from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'ArchonsWebsite/index.html')

def socials(request):
    return render(request, 'ArchonsWebsite/socials.html')

def robots(request):
    return render(request, 'ArchonsWebsite/robots.txt')

def projects(request):
    return render(request, 'ArchonsWebsite/projects.html')

def whoami(request):
    return render(request, 'ArchonsWebsite/whoami.html')

class projectsClass():
    def ArchonsWebsite(request):
        return render(request, 'ArchonsWebsite/projects/ArchonsWebsite.html')

    def cs11FinalProject(request):
        return render(request, 'ArchonsWebsite/projects/cs11FinalProject.html')

    def FileTransfer(request):
        return render(request, 'ArchonsWebsite/projects/FileTransfer.html')
    
    def ISO8601ifier(request):
        return render(request, 'ArchonsWebsite/projects/ISO8601ifier.html')
    
    def crinList(request):
        return render(request, 'ArchonsWebsite/projects/crinList.html')

    def yato(request):
        return render(request, 'ArchonsWebsite/projects/yato.html')
    
    def leetCode(request):
        return render(request, 'ArchonsWebsite/projects/leetcode.html')
    
    def WaterlooCCC(request):
        return render(request, 'ArchonsWebsite/projects/WaterlooCCC.html')