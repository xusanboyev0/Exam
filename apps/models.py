from django.db import models
from django.db.models import CASCADE
from django_ckeditor_5.fields import CKEditor5Field


# class Friend(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     photo = models.ImageField(upload_to='friends/%Y/%m/%d/')
#     proffesion = CKEditor5Field()


class TimeLine(models.Model):
    year = models.IntegerField()
    title = models.CharField(max_length=255)
    body = CKEditor5Field()
    month = models.DateField()