"""Every address of the site. Each app adds its own pages with include()."""

from django.contrib import admin
from django.urls import path

from config.health import health

urlpatterns = [
    path("admin/", admin.site.urls),
    path("health/", health, name="health"),
]
