from rest_framework import generics
from actorApp.models import actor
from actorApp.serializers import ActorSerializer
from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest

@api_view(['GET'])
def getAllActor(self):
    try:
        firstIndex =0
        limitIndex = 100
        queryset = actor.objects.all()[firstIndex:limitIndex]
        result = ActorSerializer(queryset, many=True)
        response = JsonResponse(result.data, safe=False)
        response["Access-Control-Allow-Origin"] = "*"
        return response
    except Exception as e:
        print(e)