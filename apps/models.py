import uuid

from django.contrib.auth.models import User
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True, related_name='tag')
    image = models.ImageField(upload_to='posts/')
    created_at = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)

    def __str__(self):
        return self.title

# class Profile(models.Model):
#     name = models.CharField(max_length=120)
#     last_name = models.CharField(max_length=120)
#     username = models.CharField(max_length=120)
#     website = models.URLField(blank=True)
#     balane = models.IntegerField()
#     amounts = models.IntegerField()
#     transaction = models.IntegerField()
#     image = models.ImageField(upload_to='profile')

#
# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.FloatField()
#     description = models.TextField()
#
#     def __str__(self):
#         return self.name
#
#
# class Order(models.Model):
#     class Status(models.TextChoices):
#         NEW = 'yengi', 'Yengi'
#         IN_PROGRESSING = 'yengi', 'Yengi'
#
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)
#     status = models.CharField(max_length=20, choices=Status.choices, default=Status.NEW)
#
#
# class NewOrder(Order):
#     proxy = True
#     verbose_name = 'yengi zakaz'
#     verbose_name_plural = 'Yengi zakazlar'
#
#
# class CancelOrder(Order):
#     proxy = True
#     verbose_name = 'bekor qilingan'
#     verbose_name_plural = 'Bekor qilingan zakazlar'
#
#
# class CompletedOrder(Order):
#     proxy = True
#     verbose_name = 'tasdiqlangan'
#     verbose_name_plural = 'tasdiqlangar zakazlar'
