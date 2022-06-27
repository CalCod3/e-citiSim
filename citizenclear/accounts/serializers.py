from rest_framework import serializers
from .models import CustomUser, Appointment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'id_number', ]

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['user', 'date_time', ]


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
    # class Meta:
       #model = Group
        #fields = ['url', 'name']


class RegisterSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            id_number=validated_data['id_number'],
            password=validated_data['password']
        )
        return user

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'id_number', 'password', ]
