from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Favorite, Auditlog


@receiver(post_save, sender=Favorite)
def save_and_update_object_receiver(sender, instance, created, **kwargs):
    """Signal receiver that helps to auto log changes to favorite model
    """

    action = 'created' if created else 'updated'
    action = 'deleted' if instance.is_deleted else action
    activity = f'{instance.title} has been {action}'
    owner = instance.owner
    favorite = instance

    audit_log_data = dict(favorite=favorite, action=action,
                          activity=activity, owner=owner)

    Auditlog.save_audit_log(**audit_log_data)
