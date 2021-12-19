# -*- coding:utf-8 -*-
from rest_framework import generics
from movieApp.models import movie#, movieAllInfo
from countryApp.models import country
from ratingApp.models import rating
from movieApp.serializers import MovieSerializer#, allMovieSerializer
from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.db.models import Q
from string import Template


def template(input: str):
    countryname = 'test'
    t = Template(
        "select movieApp_movie.mid as id,movieApp_movie.title,movieApp_movie.m_intro,movieApp_movie.poster from movieApp_movie  join countryApp_country on movieApp_movie.mid  = countryApp_country.mid where countryApp_country.c_name = $countryname")
    return t.substitute(countryname='"' + input + '"')


@api_view(['GET'])
def getAll(self):
    try:
        firstIndex = 0
        limitIndex = 100
        queryset = movie.objects.all().order_by('-mid')[firstIndex:limitIndex]
        result = MovieSerializer(queryset, many=True)
        response = JsonResponse(result.data, safe=False)
        response["Access-Control-Allow-Origin"] = "*"
        return response
    except Exception as e:
        print(e)


@api_view(['GET'])
def getAllRating(self):
    try:
        firstIndex = 0
        limitIndex = 100
        query1 = list(rating.objects.values_list('mid').order_by('-r_name')[firstIndex:limitIndex])
        query2 = list(movie.objects.filter(mid__in=query1).select_related('mid', 'title', 'm_intro','poster','r_name'))

        #query2 = list(movieAllInfo.objects.order_by('r_name'))
        #result = MovieSerializer(query2, many=True)


        response = JsonResponse(query2, safe=False)
        response["Access-Control-Allow-Origin"] = "*"
        print("done")
        return response
    except Exception as e:
        print(e)


@api_view(['POST'])
def getAllMovieByCountry(request):
    try:
        countryid = int(request.data.get('countryid', None))
        countryname = str(request.data.get('countryname', None))
        offset = int(request.data['pagenumber'])
        items_per_page = int(request.data.get('pagelimit', 2000))
        items_per_page = items_per_page if items_per_page < 2000 else 2000
        # movieIDList = list(country.objects.filter(c_name=countryname).values_list('mid', flat=True))
        test = template(countryname)
        a = "select movieApp_movie.mid as id,movieApp_movie.title,movieApp_movie.m_intro,movieApp_movie.poster from movieApp_movie join countryApp_country on movieApp_movie.mid  = countryApp_country.mid where countryApp_country.c_name like '" + countryname + "' order by movieApp_movie.mid offset " + str(
            offset) + " rows fetch next  " + str(items_per_page) + " rows only"
        movieList = movie.objects.raw(a)

        result = MovieSerializer(movieList, many=True)
        response = {}
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
        response['data'] = result.data
        return JsonResponse(response)
    except Exception as e:
        print(e)
