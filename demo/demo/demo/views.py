from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.http import HttpRequest,JsonResponse
import json

class UserViews(APIView):
    def post(self,request):

        # data is dictionary 
        data=json.loads(request.body)

        username=data.get("username")
        password=data.get("passwor")
        user=User.objects.create_user(username=username,password=password)

        return JsonResponse(
            {"message":"User saved Successfully","data":user},
            status=200,
            )
