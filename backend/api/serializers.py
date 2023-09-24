from django.contrib.auth.models import User
from rest_framework import serializers
from .models import File


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username']


class FileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = File
        fields = '__all__'
