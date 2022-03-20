from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Userr
from rest_framework.decorators import api_view
from .serializer import UserrSerializer



#get--> returns all the users in the model
#post--> to create new employee
class Userrlist(APIView):

    def get(self,request):
        userA=Userr.objects.all()
        seralize=UserrSerializer(userA,many=True)
        return Response(seralize.data)

    # def get(self,response):
    #     pass
# Create your views here.


