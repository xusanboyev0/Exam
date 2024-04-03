from django.urls import path

from apps import views
from apps.views import index_view

urlpatterns = [
    path('', views.index_view, name='index')
]