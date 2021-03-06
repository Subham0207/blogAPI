from typing import OrderedDict
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.custom_renderer import JPEGRenderer, PNGRenderer
from .models import blog
from .serializer import blogSerializer,filterSerializer, idSerializer, tagSerialzier, tagandtitleSerializer

# Create your views here.
class blogView(APIView):
    def get(self,req):#Get all the blogs
        blogs = blog.objects.all()
        serializer = blogSerializer(blogs,many=True)
        return Response(serializer.data)

    def post(self,req):#Add a blog
        new_blog_serializer = blogSerializer(data = req.data)
        if new_blog_serializer.is_valid():
            new_blog_serializer.save()
            return Response(new_blog_serializer.data)
        return Response(new_blog_serializer.errors)


class blog_filterbytitle_view(APIView):#title is passed as param
    def get(self,req):
        serializer = filterSerializer(data = req.query_params)#json to dict
        if serializer.is_valid():
            # print(serializer.data['search'])
            queryset = blog.objects.filter(title__icontains=serializer.data["search"])
            # print("Hello ",queryset)#data is searched successfully
            serializer2 = blogSerializer(queryset,many=True)#queryset to dict 
            return Response(serializer2.data)#dict to jsons


class blog_returnFirstTen_view(APIView):#returns 10 latest blog
    def get(self,req):
        serializer = blogSerializer(blog.objects.all().order_by('-date')[:3],many=True)
        return Response(serializer.data)

#This implementation of Update is not recommended
class blog_incViews_view(APIView):#on blog visit view is increased
    def put(self,req):
        #getting the entry using id
        serializer = idSerializer(data = req.data)
        if serializer.is_valid():
            queryset = blog.objects.filter(id=serializer.data["id"])
            serializer2 = blogSerializer(queryset,many=True)
            serializer2.data[0]["views"] += 1#increamenting viewcolumn

            #setting the view coloumn using id
            blog.objects.filter(id=serializer.data["id"]).update(views=serializer2.data[0]["views"])
            
            return Response(serializer2.data)

class blog_getMostViewedblog(APIView):#returns most blog with most views
    def get(self,req):
        serializer = blogSerializer(blog.objects.all().order_by("-views","-date")[:1],many=True)# "neg" means desc 
        return Response(serializer.data)

class blog_filterbyTag_view(APIView):
    def get(self,req):
        serializer = tagSerialzier(data = req.query_params)
        if serializer.is_valid():
            arr = serializer.data['tag'].split(' ')
            # print(arr)
            l = []
            for i in arr:
                queryset = blog.objects.filter(tags__icontains=i)
                serializer2 = blogSerializer(queryset,many=True)
                for j in range(len(serializer2.data)):
                    if serializer2.data[j] not in l:
                        l.append(serializer2.data[j])
            return Response(l)

class blog_filterByTagAndTitle_view(APIView):
    def get(self,req):
        #filter by title
        serializer = tagandtitleSerializer(data = req.query_params)#json to dict
        l = []
        if serializer.is_valid():
            queryset = blog.objects.filter(title__icontains=serializer.data["tagandtitle"])
            serializer2 = blogSerializer(queryset,many=True)#queryset to dict 
            l+=serializer2.data

        #filter by tag        
        serializer = tagandtitleSerializer(data = req.query_params)
        if serializer.is_valid():
            arr = serializer.data['tagandtitle'].split(' ')
            for i in arr:
                queryset = blog.objects.filter(tags__icontains=i)
                serializer2 = blogSerializer(queryset,many=True)
                for j in range(len(serializer2.data)):
                    if serializer2.data[j] not in l:
                        l.append(serializer2.data[j])
            return Response(l)

class blog_getblogbyid_View(APIView):
    def get(self,req):
        queryset = blog.objects.get(id=req.query_params['id'])
        serializer = blogSerializer(queryset)

        return Response(serializer.data)

class blog_authorimg_View(APIView):
    renderer_classes = [JPEGRenderer,PNGRenderer]
    def get(self,req):
        queryset = blog.objects.get(id=req.query_params['id']).img_author
        return Response(queryset)

class blog_blogimg_View(APIView):
    renderer_classes = [JPEGRenderer,PNGRenderer]
    def get(self,req):
        queryset = blog.objects.get(id=req.query_params['id']).img_blog
        return Response(queryset)