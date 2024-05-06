""" BlogPost serializer """
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import BlogPost, User


UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    Serializes a user object
    """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')

        def create(self, validated_data):
            """
            Create and return a new user with encrypted password
            """
            user = UserModel.objects.create_user(
                    username=validated_data['username'],
                    password=validated_data['password'],
                    email=validated_data['email'],
                    first_name=validated_data['first_name'],
                    last_name=validated_data['last_name'],
                    )

            return user


class BlogPostSerializer(serializers.ModelSerializer):
    """
    Serializes a blog post
    """
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        """
        Meta class
        """
        model = BlogPost
        fields = '__all__'
