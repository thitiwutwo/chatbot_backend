from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Files
        fields = '__all__'