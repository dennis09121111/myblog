from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def profile_creater(sender, created, instance, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)
        instance.profile.save()
