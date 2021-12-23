from django.shortcuts import render
from rest_framework import generics
from favoriteApp.models import favorite
from favoriteApp.serializers import favoriteSerializer
from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
# Create your views here.
@api_view(['POST'])
def insertfavorite(request):
    try:
        userid = int(request.data.get('uid', None))
        movieid = int(request.data.get('mid', None))
        favoriteSearch = favorite.objects.filter(uid=userid,mid=movieid)
        if len(favoriteSearch)<1:
            favoriteList = favorite.objects.create(uid=userid,mid=movieid)
            result = favoriteList(favoriteList, many=True)
            response = {}
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "POST"
            response["Access-Control-Max-Age"] = "1000"
            response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
            response['data'] = result.data
            return JsonResponse(response)
        else:
            response = {}
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "POST"
            response["Access-Control-Max-Age"] = "1000"
            response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
            response['data'] = ''
            return JsonResponse(response)

        return JsonResponse(response)
    except Exception as e:
        print(e)