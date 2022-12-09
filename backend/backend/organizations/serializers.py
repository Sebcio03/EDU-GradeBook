from rest_framework import serializers

from backend.organizations.models import Membership, Organization

class CreateOrUpdateOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['logo', 'name', 'address', 'phone_number']

    def create(self, validated_data: dict) -> Organization:
        user = self.context['request'].user
        organization = super().create(validated_data) 
        
        Organization.members.through.objects.create(
            organization_id=organization.id,
            user=user,
            user_type=Membership.Types.OWNER
        )
        
        return organization
    

class ListOrganizationSerializer(serializers.ModelSerializer):
    user_type = serializers.SerializerMethodField()
    
    class Meta:
        model = Organization
        fields = ['id', 'name']

    def get_user_type(self, obj: Organization) -> Membership.Types:
        user = self.context['request'].user
        return obj.members.get(user=user).user_type


class RetrieveOrganizationSerializer(serializers.ModelSerializer):
    user_type = serializers.SerializerMethodField()

    class Meta:
        model = Organization
        fields = ['logo', 'name', 'address', 'phone_number']

    def get_user_type(self, obj: Organization) -> Membership.Types:
        user = self.context['request'].user
        return obj.members.get(user=user).user_type
    