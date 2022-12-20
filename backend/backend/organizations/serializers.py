from django.db import transaction, IntegrityError

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from backend.organizations.models import Membership, Organization


class CreateOrUpdateOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ["id", "logo", "name", "address", "phone_number", "type", "country", "description"]

    @transaction.atomic()
    def create(self, validated_data: dict) -> Organization:
        user = self.context["request"].user

        try:
            organization = super().create(validated_data)
        except IntegrityError:
            raise ValidationError({'detail': ['Organization with following name and address already exists.']})

        Organization.members.through.objects.create(
            organization_id=organization.id, user=user, user_type=Membership.Types.OWNER
        )
        return organization


class ListOrganizationSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='get_type_display')
    user_type = serializers.SerializerMethodField()

    class Meta:
        model = Organization
        fields = ["id", "logo", "type", "name", "user_type"]

    def get_user_type(self, obj: Organization) -> Membership.Types:
        user = self.context["request"].user
        return obj.members.through.objects.get(organization_id=obj.id, user_id=user.id).get_user_type_display()


class RetrieveOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ["logo", "name", "address", "phone_number"]
        
