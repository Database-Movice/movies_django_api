from rest_framework import generics
from yearApp.models import year
from typeApp.serializers import typeSerializer ,onltTypeSerializer
from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest

@api_view(['GET'])
def getAllYear(self):
    try:
        firstIndex =0
        limitIndex = 100
        queryset = list(year.objects.values('y_name').distinct().order_by('y_name'))#[firstIndex:limitIndex]
        #result = onltTypeSerializer(queryset, many=True)
        response = JsonResponse(queryset, safe=False)
        response["Access-Control-Allow-Origin"] = "*"
        return response
    except Exception as e:
        print(e)