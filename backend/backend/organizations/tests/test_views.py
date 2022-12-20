from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from backend.users.models import User
from backend.users.tests.factories import UserFactory
from backend.organizations.models import Organization, Membership
from backend.organizations.tests.factories import OrganizationFactory, MembershipFactory
from backend.utils.models import Country
from backend.utils.testing import create_tmp_img


class TestListOrganizations(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.url = reverse('organizations:organization-list')

        self.user = UserFactory.create()
        self.client.force_authenticate(self.user)

    def test_list_organizations_successfully(self) -> None:
        random_user = UserFactory.create()
        org1 = OrganizationFactory.create(
            logo=create_tmp_img('logo'),
            name='t1',
            address='t2',
            phone_number='t3',
            country=Country.objects.get(shortcut='PL'),
            type=Organization.Types.COLLEGE,
        )
        membership1 = MembershipFactory.create(organization=org1, user=self.user, user_type=Membership.Types.OWNER)
        org2 = OrganizationFactory.create(
            logo=create_tmp_img('logo'),
            name='t1',
            address='t3',
            phone_number='t3',
            country=Country.objects.get(shortcut='GB'),
            type=Organization.Types.HIGH_SCHOOL,
        )
        membership2 = MembershipFactory.create(organization=org2, user=self.user, user_type=Membership.Types.ADMIN)
        org3 = OrganizationFactory.create(
            logo=create_tmp_img('logo'),
            name='t12',
            address='t3',
            phone_number='t3',
            country=Country.objects.get(shortcut='DE'),
            type=Organization.Types.ELEMENTARY_SCHOOL,
        )
        MembershipFactory.create(organization=org3, user=random_user, user_type=Membership.Types.TEACHER)
        response_body = [
            {
                "id": org1.id,
                "logo": org1.logo.url,
                "type": org1.get_type_display(),
                "name": org1.name,
                "user_type": membership1.get_user_type_display(),
            },
            {
                "id": org2.id,
                "logo": org2.logo.url,
                "type": org2.get_type_display(),
                "name": org2.name,
                "user_type": membership2.get_user_type_display(),
            },
        ]

        r = self.client.get(self.url)

        self.assertEqual(r.data, response_body)
        self.assertEqual(r.status_code, status.HTTP_200_OK)


class TestRetrieveOrganizations(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.url_name = 'organizations:organization-detail'

        self.user = UserFactory.create()
        self.client.force_authenticate(self.user)

    def test_retrieve_organization_successfully(self) -> None:
        org1 = OrganizationFactory.create(
            logo=create_tmp_img('logo'),
            name='t1',
            address='t2',
            phone_number='t3',
            country=Country.objects.get(shortcut='PL'),
            type=Organization.Types.COLLEGE,
        )
        membership1 = MembershipFactory.create(organization=org1, user=self.user, user_type=Membership.Types.OWNER)
        response_body = {
            "logo": org1.logo.url,
            "name": org1.name,
            "address": org1.address,
            "phone_number": org1.phone_number,
        }

        r = self.client.get(reverse(self.url_name, kwargs={'pk': org1.id}))

        self.assertEqual(r.data, response_body)
        self.assertEqual(r.status_code, status.HTTP_200_OK)


class TestCreateOrganizations(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.url = reverse('organizations:organization-list')

        self.user = UserFactory.create()
        self.client.force_authenticate(self.user)

    def test_create_organization_successfully(self) -> None:
        request_body = {
            "logo": create_tmp_img('logo'),
            "name": "Harvard University",
            "address": "Warsaw",
            "phone_number": "123123123",
            "type": "C",
            "country": "PL",
        }

        r = self.client.post(self.url, request_body)

        organization = Organization.objects.filter(
            name=request_body['name'],
            address=request_body['address'],
            phone_number=request_body['phone_number'],
            type=request_body['type'],
            country=Country.objects.get(shortcut=request_body['country']),
            logo__isnull=False,
        )
        self.assertTrue(organization.exists())
        membership = Membership.objects.filter(
            organization=organization.first(),
            user=self.user,
            user_type=Membership.Types.OWNER.value
        )
        self.assertTrue(membership.exists())
        self.assertEqual(r.status_code, status.HTTP_201_CREATED)
