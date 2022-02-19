from rest_framework import serializers
from .models import UserGallery,User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class UserGallerySerializer(serializers.ModelSerializer):

    class Meta:
        model= UserGallery
        fields= '__all__'