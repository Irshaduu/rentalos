from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    """Who signs in. Their roles and the sign-in page come with step 1 (docs/PLAN.md)."""

    name = "apps.users"
    verbose_name = _("Users")
