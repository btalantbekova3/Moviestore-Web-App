from django.test import TestCase

# Create your tests here.
from django.urls import path

from djangoProject.urls import urlpatterns
from . import views

urlpatterns = [
    path('', views.index, name='movies.index'),
]