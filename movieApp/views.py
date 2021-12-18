# -*- coding:utf-8 -*-
from rest_framework import generics
from movieApp.models import movie
from movieApp.serializers import MovieSerializer
from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest

@api_view(['GET'])
def getAll(self):
    try:
        firstIndex =0
        limitIndex = 100
        queryset = movie.objects.all()[firstIndex:limitIndex]
        result = MovieSerializer(queryset, many=True)
        response = JsonResponse(result.data, safe=False)
        response["Access-Control-Allow-Origin"] = "*"
        return response
    except Exception as e:
        print(e)

def getAllYear(self):
    try:
        queryset = movie.objects.all()
        serializer_class = MovieSerializer
        print("done")
    except Exception as e:
        print(e)


