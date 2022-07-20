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


class ProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    rating = serializers.IntegerField(default=0)
    status = serializers.CharField(default='', max_length=127, allow_blank=True, allow_null=True)
    description = serializers.CharField(default='', max_length=511, allow_blank=True, allow_null=True)

    class Meta:
        model = Profile
        fields = ['rating', 'status', 'description']

    def create(self, validated_data):
        return Profile.objects.create(user_id=self.user_id,)
