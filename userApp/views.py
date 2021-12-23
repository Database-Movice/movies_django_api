from rest_framework import generics
from userApp.models import user
from userApp.serializers import userSerializer
from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest

@api_view(['POST'])
def createUser(request):
    try:
        username = str(request.data.get('uname', None))
        userpassword = str(request.data.get('upwd', None))
        uid = user.objects.count()+1
        userlist = user.objects.create(uid=uid ,uname=username,upwd=userpassword)

        result = userSerializer(userlist, many=True)
        response = {}
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
        response['data'] = result.data
        return JsonResponse(response)
    except Exception as e:
        print(e)
@api_view(['POST'])
def userLogin(request):
    try:
        username = str(request.data.get('uname', None))
        userpassword = str(request.data.get('upwd', None))

        userlist = user.objects.filter(uname=username,upwd=userpassword)
        if len(userlist)<1:
            response = {}
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "POST"
            response["Access-Control-Max-Age"] = "1000"
            response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
            response['data'] = 'username or password is wrong'
            return JsonResponse(response)
        else:
            result = userSerializer(userlist, many=True)
            response = {}
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "POST"
            response["Access-Control-Max-Age"] = "1000"
            response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
            response['data'] = result.data
            return JsonResponse(response)
    except Exception as e:
        print(e)