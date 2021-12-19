from rest_framework import generics
from typeApp.models import type
from typeApp.serializers import typeSerializer ,onltTypeSerializer
from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest

@api_view(['GET'])
def getAllType(self):
    try:
        firstIndex =0
        limitIndex = 100
        queryset = list(type.objects.values('t_name').distinct())#[firstIndex:limitIndex]
        #result = onltTypeSerializer(queryset, many=True)
        response = JsonResponse(queryset, safe=False)
        response["Access-Control-Allow-Origin"] = "*"
        return response
    except Exception as e:
        print(e)