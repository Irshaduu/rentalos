"""The entry point for a WSGI server, such as gunicorn on the host.

It points to the production settings, which come with going live
(docs/PLAN.md), so a server that is not told otherwise never runs with a
developer's settings.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")

application = get_wsgi_application()
