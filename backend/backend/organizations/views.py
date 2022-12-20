from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from backend.organizations.models import Organization
from backend.organizations.permissions import IsOrganizationOwner
from backend.organizations.serializers import (
    CreateOrUpdateOrganizationSerializer,
    ListOrganizationSerializer,
    RetrieveOrganizationSerializer,
)


class OrganizationViewSet(ModelViewSet):
    def get_queryset(self):
        user = self.request.user
        return Organization.objects.prefetch_related("members").filter(members=user).all()

    def get_permissions(self) -> list:
        match self.request.method:
            case "PUT" | "PATCH" | "DELATE":
                return [IsOrganizationOwner()]
            case _:
                return [IsAuthenticated()]

    def get_serializer_class(self):
        match self.action:  
            case "update" | "update_partial" | "create":
                return CreateOrUpdateOrganizationSerializer
            case "list":
                return ListOrganizationSerializer
            case "retrieve":
                return RetrieveOrganizationSerializer
