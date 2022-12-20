from rest_framework.permissions import IsAuthenticated

from backend.organizations.models import Organization, Membership


class IsOrganizationAdmin(IsAuthenticated):
    def has_object_permission(self, request, view, obj: Organization):
        return obj.members.through.objects. filter(user_type=Membership.Types.ADMIN, user=request.user).exists()


class IsOrganizationOwner(IsAuthenticated):
    def has_object_permission(self, request, view, obj: Organization):
        return obj.members.through.objects.filter(user_type=Membership.Types.OWNER, user=request.user).exists()
