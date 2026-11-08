import uuid
from django.db import models


class UUIDPrimaryKeyModel(models.Model):
    """UUID primary key for safer external references and future distribution."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class TimeStampedModel(models.Model):
    """Common created / updated timestamps."""
    cree_le = models.DateTimeField(auto_now_add=True)
    mis_a_jour_le = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True