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

    def __str__(self):
        return self.name


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

    is_deleted = models.BooleanField(null=True, default=False)

    class Meta:
        unique_together = [['title', 'owner', 'is_deleted']]

        ordering = ['ranking', 'category']

    def __str__(self):

        return f"{self.owner}'s, {self.title}"


class Auditlog(AbstractBaseModel):

    favorite = models.ForeignKey(
        Favorite, on_delete=models.CASCADE, related_name="audit_logs")
    action = models.TextField()
    activity = models.TextField()
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='audit_logs')

    @staticmethod
    def save_audit_log(**kwargs):
        new_audit_log = Auditlog(**kwargs)
        new_audit_log.save()
