from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.deletion import CASCADE


class ProfilePage(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    subject = GenericForeignKey('content_type', 'object_id')
