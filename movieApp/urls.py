from movieApp.views import *
from django.urls import path


urlpatterns = [
    path('getallmovie/', getAll),
    path('getallYear/', getAllYear),
]


