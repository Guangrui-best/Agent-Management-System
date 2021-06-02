from rest_framework import serializers
from users.models import CustomUser


class UserDisplaySerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = CustomUser.objects.create_user(validated_data['username'], validated_data['email'])
        return user

    class Meta:
        model = CustomUser
        fields = ["id", "username", "email"]