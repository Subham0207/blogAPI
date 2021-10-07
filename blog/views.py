from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import blog
from .serializer import blogSerializer,filterSerializer

# Create your views here.
class blogView(APIView):
    def get(self,req):
        blogs = blog.objects.all()
        serializer = blogSerializer(blogs,many=True)
        return Response(serializer.data)

    def post(self,req):
        new_blog_serializer = blogSerializer(data = req.data)
        if new_blog_serializer.is_valid():
            new_blog_serializer.save()
            return Response(new_blog_serializer.data)
        return Response(new_blog_serializer.errors)


class blog_filterbytitle_view(APIView):
    def get(self,req):
        serializer = filterSerializer(data = req.query_params)#json to dict
        if serializer.is_valid():
            # print(serializer.data['search'])
            queryset = blog.objects.filter(title__icontains=serializer.data["search"])
            # print("Hello ",queryset)#data is searched successfully
            serializer2 = blogSerializer(queryset,many=True)#queryset to dict 
            return Response(serializer2.data)#dict to jsons


class blog_returnFirstTen_view(APIView):
    def get(self,req):
        serializer = blogSerializer(blog.objects.all().order_by('-date')[:10],many=True)
        return Response(serializer.data)


