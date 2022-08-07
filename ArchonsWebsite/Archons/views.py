from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def socials(request):
    return render(request, 'socials.html')

def robots(request):
    return render(request, 'robots.txt')

def projects(request):
    return render(request, 'projects.html')

class projectsClass():
    def ArchonsWebsite(request):
        return render(request, 'projects/ArchonsWebsite.html')

    def cs11FinalProject(request):
        return render(request, 'projects/cs11FinalProject.html')

    def FileTransfer(request):
        return render(request, 'projects/FileTransfer.html')
    
    def ISO8601ifier(request):
        return render(request, 'projects/ISO8601ifier.html')
    
    def crinList(request):
        return render(request, 'projects/crinList.html')

    def yato(request):
        return render(request, 'projects/yato.html')
    
    def leetCode(request):
        return render(request, 'projects/leetcode.html')
    
    def WaterlooCCC(request):
        return render(request, 'projects/WaterlooCCC.html')