from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("upload", views.upload, name="upload"),
    path("confirmDownload/<str:file_uuid>", views.confirmDownload, name="confirmDownload"),
]