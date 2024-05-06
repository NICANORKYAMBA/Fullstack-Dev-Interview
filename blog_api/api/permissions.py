""" BlogPost permissions """
from rest_framework.permissions import BasePermission, SAFE_METHODS


class BlogPostPermission(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_permission(self, request, view):
        """
        Check if the user has permission to perform the action.

        Args:
            request (HttpRequest): The request object.
            view (View): The view object.

        Returns:
            bool: True if the user has permission, False otherwise.
        """
        if request.method in SAFE_METHODS:
            return True

        if request.user and request.user.is_authenticated:
            if request.method == 'POST':
                return request.user.groups.filter(name='Editors').exists()
            else:
                return request.user == view.get_object().author or request.user.groups.filter(name='Admins').exists()

        return False
