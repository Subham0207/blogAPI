from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework.fields import SerializerMethodField
from rest_framework.views import APIView
from .models import employees
from .serializer import employeeSerializer
from rest_framework.response import Response

from getpost import serializer

# Create your views here.
class employeelist(APIView):
    def get(self,req):
        employee1 = employees.objects.all()
        serializer = employeeSerializer(employee1,many=True)

        return Response(serializer.data)

    def post(self,req):
        # print("Hey here is your data ",req.data)
        serializer = employeeSerializer(data = req.data)#JSON to queryset
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class employeeDetails(APIView):
    def get(self,req):
        queryset = employees.objects.filter(firtname="subham")
        serializer = employeeSerializer(queryset,many=True)#queryset to dict
        return Response(serializer.data)#reponse class has dict to json conversion
