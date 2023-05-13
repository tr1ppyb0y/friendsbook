from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save
from django.dispatch import receiver

from business.models import Business
from useraccount.models import UserAccount


class ProfilePage(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    subject = GenericForeignKey('content_type', 'object_id')


@receiver(post_save, sender=UserAccount)
def create_user_profile(instance, created, **kwargs):
    if created:
        ProfilePage.objects.create(subject=instance)


@receiver(post_save, sender=Business)
def create_business_profile(instance, created, **kwargs):
    if created:
        ProfilePage.objects.create(subject=instance)