"""The base that every model in our apps builds on."""

import uuid

from django.db import models
from django.db.models.functions import UUID7


class BaseModel(models.Model):
    """Gives a model its key: a UUID7 (ADR-0008).

    Python makes the key when the record is created, so records can be linked
    to each other before they are saved, one by one or in bulk. PostgreSQL
    makes one for a row added outside Django. A UUID7 never repeats on any
    server, so a business can move from one server to another.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid7, db_default=UUID7(), editable=False)

    class Meta:
        abstract = True
