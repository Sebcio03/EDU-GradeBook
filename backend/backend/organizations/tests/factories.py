from factory.django import DjangoModelFactory
from backend.organizations.models import Organization, Membership


class OrganizationFactory(DjangoModelFactory):
    class Meta:
        model = Organization


class MembershipFactory(DjangoModelFactory):
    class Meta:
        model = Membership
