from asyncio import SendfileNotAvailableError
from django.db.models.signals import post_save
from django.contrib.auth.models import User #The User is te sender of the signal
from django.dispatch import receiver #This will be the reciever
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()