from django.db import models
from django.utils.translation import gettext_lazy as _
from backend.users.models import User


class Organization(models.Model):
    logo = models.ImageField()
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

    members = models.ManyToManyField(User, through="Membership")


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
        constraints = [models.UniqueConstraint(fields=["organization", "user"], name="ogranization2user_unique")]
