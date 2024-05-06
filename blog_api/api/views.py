""" BlogPost views """
from rest_framework import viewsets, permissions
from .models import BlogPost
from .serielizers import BlogPostSerializer
from .permissions import BlogPostPermission


class BlogPostViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows posts to be viewed or edited. """
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [BlogPostPermission]

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
