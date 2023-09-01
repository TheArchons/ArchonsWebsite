from django.shortcuts import render
from django import forms
import os
from os.path import exists
import base64
from django.http import FileResponse, HttpResponse
from datetime import datetime
from django.shortcuts import redirect
import uuid
from .models import File

files_directory = os.getcwd() + "/Archons/static/filetransfer/files/"


# Create your views here.
class fileUploadForm(forms.Form):
    file = forms.FileField(label='')
    should_randomize_filename = forms.BooleanField(required=False, initial=False)


def index(request):
    return render(request, 'filetransfer/index.html')


def upload(request):
    if request.method == "POST":
        form = fileUploadForm(request.POST, request.FILES)
        print(request.FILES['file'].file)
        if form.is_valid():
            file = form.cleaned_data['file']

            file_directory = files_directory + str(form.cleaned_data['file'])

            # Add the file to the database
            file_uuid = str(uuid.uuid4().hex)
            if form.cleaned_data['should_randomize_filename']:
                # set the file name to the uuid, but keep the file extension
                file.name = f"{str(file_uuid)}.{file.name.split('.')[-1]}"

            file_name = str(form.cleaned_data['file'])
            file_data = File(uuid=file_uuid, name=file_name, uploaded_at=datetime.now())
            file_data.save()

            # Make the file directory
            # We have to store it in the directory so the downloaded file has the same name as the uploaded file
            file_directory = files_directory + file_uuid
            os.makedirs(file_directory)

            file_directory_and_name = f"{file_directory}/{file_name}"

            # Save the file
            with open(file_directory_and_name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)

            url = 'https://' + request.get_host()
            return render(request, 'filetransfer/uploaded.html', {'url': url + '/confirmDownload/' + file_uuid})
        else:
            # print errors
            print(form.errors)
            return render(request, 'filetransfer/error.html', {'error': form.errors})
    else:
        return render(request, 'filetransfer/upload.html',
                      {'form': fileUploadForm()})


def confirmDownload(request, file_uuid):
    file_name = File.objects.get(uuid=file_uuid).name
    download_url = f"/static/filetransfer/files/{file_uuid}/{file_name}"
    upload_date = File.objects.get(uuid=file_uuid).uploaded_at
    return render(request, 'filetransfer/confirmDownload.html',
                  {'downloadURL': download_url, 'filename': file_name, 'uploadDate': upload_date})
