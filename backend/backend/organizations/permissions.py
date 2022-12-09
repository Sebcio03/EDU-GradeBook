from rest_framework.permissions import IsAuthenticated

from backend.organizations.models import Organization

class IsOrganizationAdmin(IsAuthenticated):
    def has_object_permission(self, request, view, obj: Organization):
        user = self.request.user
        return obj.owner == user or user in obj.members

class IsOrganizationOwner(IsAuthenticated):
    def has_object_permission(self, request, view, obj: Organization):
        return obj.owner == self.request.user