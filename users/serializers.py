from rest_framework import serializers
from .models import Users
from . import models
from django.contrib.auth.hashers import make_password

class UsersSerializer(serializers.ModelSerializer):


    class Meta:
        model = Users
        fields = ('id','name','email','password')


    def create(self, validated_data):
        user = models.Users(
            name=validated_data["name"],
            email=validated_data["email"],
            password=make_password(validated_data["password"]),
        )
        user.save()
        return user
