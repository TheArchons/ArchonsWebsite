from django.db import models


# Create your models here.
class File(models.Model):
    uuid = models.CharField(max_length=256, unique=True)
    name = models.FileField(upload_to='files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
