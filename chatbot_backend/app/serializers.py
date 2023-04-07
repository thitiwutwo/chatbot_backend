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

class ChannelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Channels
        fields = '__all__'


class ChatSerializer(serializers.ModelSerializer):
    # channel = ChannelSerializer()
    class Meta:
        model = Chats
        fields = ('__all__')


