from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from . models import SchoolBoard

User = settings.AUTH_USER_MODEL

@receiver(post_save, sender=User)
def create_board(sender, instance, created, **kwargs):
    if created:
        SchoolBoard.objects.create(user=instance)