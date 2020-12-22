from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsMemberGroup(BasePermission):
    """Admin or group member
    """
    def has_object_permission(self, request, view, obj):
        return request.user in obj.group.members.all() or obj.group.founder == request.user


class IsAuthorEntry(BasePermission):
    """Author of entry or Admin
    """
    def has_object_permission(self, request, view, obj):
        return self.obj.user == request.user or obj.group.founder == request.user


class IsAuthorCommentEntry(BasePermission):
    """Author of comment to entry or Admin
    """
    def has_object_permission(self, request, view, obj):
        return self.obj.user == request.user or obj.entry.group.founder == request.user


class IsAuthor(BasePermission):
    """Author of comment or entry
    """
    def has_permission(self, request, view):
        if request.method == permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
