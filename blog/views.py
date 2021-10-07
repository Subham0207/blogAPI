from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import blog
from .serializer import blogSerializer

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