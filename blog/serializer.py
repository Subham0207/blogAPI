from django.db.models import fields
from rest_framework import serializers
from .models import blog

class blogSerializer(serializers.ModelSerializer):
    class Meta:
        model = blog
        fields = '__all__'

class filterSerializer(serializers.Serializer):
    search = serializers.CharField(max_length=50)



class idSerializer(serializers.Serializer):
    id = serializers.IntegerField()