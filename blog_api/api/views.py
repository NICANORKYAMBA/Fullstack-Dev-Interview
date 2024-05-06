""" BlogPost views """
from rest_framework import viewsets, permissions
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.schemas import openapi
from rest_framework.response import Response
from .models import BlogPost
from .serielizers import BlogPostSerializer, UserSerializer
from .permissions import BlogPostPermission


def api_root(request):
    """
    API root.

    Args:
        request (HttpRequest): The request object.

    Returns:
        Response: The response object with the welcome message.
    """
    info = openapi.get_api_root_as_dict(request.user)
    info['message'] = 'Welcome to my Blog Post REST API!'
    return Response(info)


class WelcomeViewSet(APIView):
    """ Welcome view """
    def get(self, request):
        """
        Get the welcome message.

        Args:
            request (HttpRequest): The request object.

        Returns:
            Response: The response object with the welcome message.
        """
        return Response({'message': 'Welcome to my Blog Post REST API!'})


class CreateUserView(CreateAPIView):
    """ API endpoint that allows users to be created. """
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer


class BlogPostViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows posts to be viewed or edited. """
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """
        Save the post when creating a new blog post.

        Args:
            serializer (BlogPostSerializer): The serializer for the blog post.

        Returns:
            None
        """
        serializer.save(author=self.request.user)


    def perform_update(self, serializer):
        """
        Save the post when updating a blog post.

        Args:
            serializer (BlogPostSerializer): The serializer for the blog post.

        Returns:
            None
        """
        serializer.save(author=self.request.user)


    def perform_destroy(self, instance):
        """
        Delete a blog post.

        Args:
            instance (BlogPost): The blog post to be deleted.

        Returns:
            None
        """
        instance.delete()


    def destroy(self, request, pk=None):
        """
        Delete a blog post.

        Args:
            request (HttpRequest): The request object.
            pk (int): The primary key of the blog post.

        Returns:
            Response: The response object with a 204 status code.
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
