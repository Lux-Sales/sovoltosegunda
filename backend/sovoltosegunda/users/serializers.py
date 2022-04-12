from rest_framework import serializers, status
from rest_framework.response import Response
from django.contrib.auth.models import User


class AddUserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=200, required=True)
    last_name = serializers.CharField(max_length=200, required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(max_length=200, required=True)

    def create(self, validated_data):
        user = User.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['email'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        del validated_data['password']
        return Response(
            {"message": "User Created", "user": validated_data},
            status=status.HTTP_201_CREATED
        )
