"""The people who sign in."""

from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel


class User(BaseModel, AbstractUser):
    """A person who signs in: a user, never a staff record (docs/GLOSSARY.md).

    Made before any other app's first migration, so it can grow later without
    rebuilding the database. Django's own is_staff only lets a person into the
    Django admin; it never means the business's staff.
    """

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
