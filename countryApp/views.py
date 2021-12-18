from rest_framework import generics
from countryApp.models import country
from countryApp.serializers import countrySerializer
from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest

@api_view(['GET'])
def getAllCountry(self):
    try:
        firstIndex =0
        limitIndex = 100
        queryset = country.objects.all()[firstIndex:limitIndex]
        result = countrySerializer(queryset, many=True)
        response = JsonResponse(result.data, safe=False)
        response["Access-Control-Allow-Origin"] = "*"
        return response
    except Exception as e:
        print(e)