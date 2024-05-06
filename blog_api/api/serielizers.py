""" BlogPost serializer """
from rest_framework import serializers
from .models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    """
    Serializes a blog post
    """
    class Meta:
        """
        Meta class
        """
        model = BlogPost
        fields = '__all__'
