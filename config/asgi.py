"""The entry point for an ASGI server.

It points to the production settings, which come with going live
(docs/PLAN.md), so a server that is not told otherwise never runs with a
developer's settings.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")

application = get_asgi_application()
