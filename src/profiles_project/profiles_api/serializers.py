from rest_framework import serializers
from . import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing out APIView"""

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile project"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        """Create and return a new user"""

        user = models.UserProfile(
            name = validated_data['name'],
            email = validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user
