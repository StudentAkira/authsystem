from rest_framework import serializers
from .models import CustomUser, Profile


class CustomUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(min_length=4)
    password = serializers.CharField(min_length=4)

    class Meta:
        model = CustomUser
        fields = ['username', 'password']

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
