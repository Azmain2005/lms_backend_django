from rest_framework.permissions import BasePermission, SAFE_METHODS

class AdminOrReadOnly(BasePermission):
    """
    Allow read-only methods for everyone.
    Only admin users (is_staff=True) can write (POST, PUT, DELETE).
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_staff
