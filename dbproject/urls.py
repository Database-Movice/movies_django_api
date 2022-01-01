"""dbproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from movieApp.views import getAll, getMovieByRating, getMovieByCountry, getMovieByType, getMovieByYear, getMovieByMid, \
    getMovieByTitle, getMovieByDirector, getMovieBySearch, getMovie,getRandomMovie,getMovieByActor
from actorApp.views import getAllActor
from directorApp.views import getAllDirector
from countryApp.views import getAllCountry
from typeApp.views import getAllType
from yearApp.views import getAllYear
from userApp.views import createUser, userLogin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('getallmovie/', getAll),
    path('getmoviebyRating/', getMovieByRating),
    path('getallActor/', getAllActor),
    path('getallDirector/', getAllDirector),
    path('getallCountry/', getAllCountry),
    path('getallType/', getAllType),
    path('getmoviebycountry/', getMovieByCountry),
    path('getallYear/', getAllYear),
    path('getmoviebytype/', getMovieByType),
    path('getmoviebyyear/', getMovieByYear),
    path('getmoviebymid/', getMovieByMid),
    path('getmoviebytitle/', getMovieByTitle),
    path('getmoviebydirector/', getMovieByDirector),
    path('getmoviebysearch/', getMovieBySearch),
    path('createuser/', createUser),
    path('userlogin/', userLogin),
    path('getmovierange/',getMovie),
    path('getRandomMovie/',getRandomMovie),
    path('getmoviebyactor/',getMovieByActor)

]
