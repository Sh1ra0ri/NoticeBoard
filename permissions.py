from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        author = getattr(obj, "author", None)
        if author is None:
            author = getattr(obj, "owner", None)

        return author == request.user or getattr(request.user, "role", "") == "admin"
