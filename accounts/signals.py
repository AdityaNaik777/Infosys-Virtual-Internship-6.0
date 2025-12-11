# accounts/signals.py
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()

@receiver(post_save, sender=User)
def handle_user_created(sender, instance, created, **kwargs):
    # No profile model exists, so nothing special to create.
    # Keep this in case you add analytics or welcome emails later.
    if created:
        print(f"New user created: {instance.username}")
