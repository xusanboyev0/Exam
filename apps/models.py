from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    group = models.CharField(max_length=50)

    def __str__(self):
        return self.name
