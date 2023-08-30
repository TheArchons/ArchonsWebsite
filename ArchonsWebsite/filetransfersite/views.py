from django.shortcuts import render
from django import forms
import os
from os.path import exists
import base64
from django.http import FileResponse, HttpResponse
from datetime import datetime
from django.shortcuts import redirect

files_directory = os.getcwd() + "/Archons/static/filetransfer/files/"

# Create your views here.
class fileUploadForm(forms.Form):
    file = forms.FileField(label='')


def index(request):
    appendIP(request)
    return render(request, 'filetransfer/index.html')


def upload(request):
    appendIP(request)
    if request.method == "POST":
        form = fileUploadForm(request.POST, request.FILES)
        print(request.FILES['file'].file)
        if form.is_valid():
            file = form.cleaned_data['file']
            file_directory = files_directory + str(form.cleaned_data['file'])
            if not exists(file_directory):
                with open(file_directory, 'wb+') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)
            else:
                return render(request, 'filetransfer/error.html', {'error': 'Error: File already exists'})
            encodedname = str(base64.b64encode(str(file).encode('utf-8')))[2:][:-1]
            url = 'https://' + request.get_host()
            print(encodedname)
            return render(request, 'filetransfer/uploaded.html', {'url': url + '/confirmDownload/' + encodedname})
        else:
            # print errors
            print(form.errors)
            return render(request, 'filetransfer/error.html', {'error': form.errors})
    else:
        return render(request, 'filetransfer/upload.html',
                      {'form': fileUploadForm()})

def confirmDownload(request, file_name):
    appendIP(request)
    print(file_name)
    file_name_decoded = base64.b64decode(file_name).decode('utf-8')
    file_directory = "/static/filetransfer/files/" + file_name_decoded
    url = 'http://' + request.get_host()
    return render(request, 'filetransfer/confirmDownload.html', {'downloadURL': url + '/download/' + file_name, 'filename': file_name_decoded, 'file_dir': file_directory})


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def appendIP(request):
    clientIP = get_client_ip(request)
    open('ip.txt', 'a').write(str(datetime.now()) + '    ' + clientIP + '\n')
