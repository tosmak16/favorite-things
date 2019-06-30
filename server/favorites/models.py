from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import JSONField
from django.core.serializers.json import DjangoJSONEncoder
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User

# Create your models here.


class AbstractBaseModel(models.Model):
    """
    An abstract base class model that provides self updating
    ``created_date`` and ``modified_date`` fields.
    """

    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)

    class Meta:

        abstract = True


class Category(AbstractBaseModel):

    name = models.TextField(unique=True)


class Favorite(AbstractBaseModel):

    title = models.TextField()

    description = models.TextField(MinLengthValidator(
        10, message="Description should be at least 10 characters"), null=True)

    ranking = models.PositiveIntegerField()

    metadata = JSONField(encoder=DjangoJSONEncoder, null=True, blank=True)

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='favorites')

    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='favorites')

    class Meta:
        unique_together = [['title', 'owner']]


class Auditlog(AbstractBaseModel):

    favourite = models.ForeignKey(
        Favorite, on_delete=models.CASCADE, related_name="audit_logs")

    action = models.TextField()
