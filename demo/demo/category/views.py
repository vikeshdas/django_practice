import json
from django.shortcuts import render
from category.models import Category
from rest_framework.views import APIView
from django.http import HttpRequest,JsonResponse

class CategoryViews(APIView):
    
    def post(self,request):
        data=json.loads(request.body)

        category=Category.objects.create(name=data.get("name"),description=data.get("description"))

        JsonResponse({"message":"data saved successfully"},status=200)


