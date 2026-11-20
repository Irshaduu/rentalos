"""Settings shared by every environment.

Values that differ between machines come from environment variables
(see config/env.py and .env.example).
"""

from pathlib import Path

from django.utils.csp import CSP
from django.utils.translation import gettext_lazy as _

from config.env import env, load_env_file

BASE_DIR = Path(__file__).resolve().parent.parent.parent

load_env_file(BASE_DIR / ".env")

SECRET_KEY = env("DJANGO_SECRET_KEY")

DEBUG = False

ALLOWED_HOSTS: list[str] = []

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Our apps, each on its floor (docs/ARCHITECTURE.md).
    "apps.core",
    "apps.users",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.csp.ContentSecurityPolicyMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    # Every page needs sign-in, unless its view is marked @login_not_required.
    "django.contrib.auth.middleware.LoginRequiredMiddleware",
    # A signed-in page is never kept by the browser, so Back after signing out
    # shows nothing private.
    "apps.users.middleware.NoStoreMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Only our own server may send scripts, styles, pictures and fonts, and no
# inline script or style runs, so a script slipped into a page cannot run.
SECURE_CSP = {
    "default-src": [CSP.SELF],
    "script-src": [CSP.SELF],
    "style-src": [CSP.SELF],
    "img-src": [CSP.SELF],
    "font-src": [CSP.SELF],
    "connect-src": [CSP.SELF],
    "object-src": [CSP.NONE],
    "base-uri": [CSP.NONE],
    "form-action": [CSP.SELF],
    "frame-ancestors": [CSP.NONE],
}

AUTH_USER_MODEL = "users.User"

# The sign-in page, built with step 1 (docs/PLAN.md). An address, not a name,
# so it also works in a test with its own addresses.
LOGIN_URL = "/sign-in/"

# Our models get a UUID7 key from apps/core/models.py (ADR-0008). This is
# only for the tables Django makes itself, like its many-to-many link tables.
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # The base layout, shared components and state pages; each app keeps
        # its own pages in its templates folder.
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# PostgreSQL 18 everywhere (ADR-0004).
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST", default="localhost"),
        "PORT": env("DB_PORT", default="5432"),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-in"

# English only until a second language is wanted (ADR-0009).
LANGUAGES = [("en", _("English"))]

LOCALE_PATHS = [BASE_DIR / "locale"]

# India time for every date the system shows or stores as "today".
TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

# Each machine sets its own mailer (local.py, test.py, production later).
# Here there is none, so a machine that forgets cannot send mail, nor print
# a sign-in or reset code into its logs.
MAILERS: dict[str, dict] = {}
