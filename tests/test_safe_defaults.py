"""Safe defaults from the first app: sign-in, a strict CSP, signed-in pages never kept by the
browser, one language, and a small admin."""

import pytest
from django.contrib import admin
from django.contrib.auth.decorators import login_not_required
from django.http import HttpResponse
from django.urls import path


def plain_page(request):
    return HttpResponse("A page nobody marked public.")


# Public: it only tests that a visitor's page is left alone, and shows nothing private.
@login_not_required
def public_page(request):
    return HttpResponse("A page marked public.")


urlpatterns = [path("plain/", plain_page), path("public/", public_page)]

#: The only models in the Django admin, and why. The admin is for emergencies.
#: A business record is never in it: it changes only through its service, so
#: every rule runs (CONTRIBUTING.md, Code rules).
ADMIN_MODELS = {
    "users.User": "set up or turn off a user",
    "auth.Group": "Django's own, for the admin's staff permissions",
}


def test_a_page_needs_sign_in_unless_it_is_marked_public(client, settings):
    settings.ROOT_URLCONF = __name__

    response = client.get("/plain/")

    assert response.status_code == 302
    assert response.url.startswith(settings.LOGIN_URL)


def test_a_page_marked_public_opens_for_a_visitor(client, settings):
    settings.ROOT_URLCONF = __name__

    assert client.get("/public/").status_code == 200


def test_every_answer_carries_a_strict_content_security_policy(client, settings):
    settings.ROOT_URLCONF = __name__

    policy = client.get("/plain/")["Content-Security-Policy"]

    assert "script-src 'self'" in policy
    assert "style-src 'self'" in policy
    assert "object-src 'none'" in policy
    assert "unsafe-inline" not in policy
    assert "unsafe-eval" not in policy


@pytest.mark.django_db
def test_a_page_shown_to_a_signed_in_person_is_never_kept_by_the_browser(
    client, settings, django_user_model
):
    settings.ROOT_URLCONF = __name__
    client.force_login(django_user_model.objects.create_user(username="someone"))

    response = client.get("/plain/")

    assert response.status_code == 200
    assert "no-store" in response["Cache-Control"]


def test_a_page_for_a_visitor_is_left_to_the_browser(client, settings):
    settings.ROOT_URLCONF = __name__

    assert "no-store" not in client.get("/public/").get("Cache-Control", "")


def test_english_is_the_only_language_until_a_second_is_wanted(settings):
    assert [code for code, _name in settings.LANGUAGES] == ["en"]
    assert settings.LOCALE_PATHS == [settings.BASE_DIR / "locale"]


def test_business_records_are_never_in_the_admin():
    assert {model._meta.label for model in admin.site._registry} == ADMIN_MODELS.keys()
