from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('getclients/', getclients.as_view(), name='getclients'),
]