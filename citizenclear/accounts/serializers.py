import email
from enum import unique
from pyexpat import model
from rest_framework import serializers
from django.contrib.auth.models import User, Group

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'first_name', 'last_name', 'email']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
class RegisterSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data['email'],
            password = validated_data['password']
        )
        return user;

    class Meta:
        model = User
        fields = ['url', 'first_name', 'last_name', 'email']
