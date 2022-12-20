from django.db import models
from django.utils.translation import gettext_lazy as _

from django.core.validators import MinLengthValidator

from backend.utils.models import Country
from backend.users.models import User


class Organization(models.Model):
    class Types(models.TextChoices):
        COLLEGE = ("C", _("College"))
        HIGH_SCHOOL = ("H", _("High School"))
        ELEMENTARY_SCHOOL = ("E", _("Elementary School"))

    logo = models.ImageField()
    name = models.CharField(max_length=255, validators=[MinLengthValidator(8)])
    address = models.CharField(max_length=100, validators=[MinLengthValidator(4)])
    phone_number = models.CharField(max_length=100, validators=[MinLengthValidator(6)])
    type = models.CharField(max_length=1, choices=Types.choices)
    country = models.ForeignKey(Country, models.CASCADE)
    description = models.TextField(null=True, blank=True)

    members = models.ManyToManyField(User, through="Membership")

    class Meta:
        constraints = [models.UniqueConstraint(fields=["name", "address"], name="name2address_unique")]


class Membership(models.Model):
    class Types(models.TextChoices):
        OWNER = ("O", _("Owner"))
        STUDENT = ("S", _("Student"))
        TEACHER = ("T", _("Teacher"))
        ADMIN = ("A", _("Administrator"))

    organization = models.ForeignKey(Organization, models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE)
    user_type = models.CharField(max_length=1, choices=Types.choices)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["organization", "user"], name="organization2user_unique")]
