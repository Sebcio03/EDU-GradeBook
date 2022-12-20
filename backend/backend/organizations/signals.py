from django.db.models.signals import post_save
from django.dispatch import receiver

from backend.users.models import User

from backend.organizations.models import Organization


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Organization.objects.create(user=instance)
