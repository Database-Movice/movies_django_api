from rest_framework import generics
from directorApp.models import director
from directorApp.serializers import directorSerializer
from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest

@api_view(['GET'])
def getAllDirector(self):
    try:
        firstIndex =0
        limitIndex = 100
        queryset = director.objects.all()[firstIndex:limitIndex]
        result = directorSerializer(queryset, many=True)
        response = JsonResponse(result.data, safe=False)
        response["Access-Control-Allow-Origin"] = "*"
        return response
    except Exception as e:
        print(e)