"""Keeps signed-in pages out of the browser's cache."""

from django.utils.cache import add_never_cache_headers


class NoStoreMiddleware:
    """Tells the browser never to keep a page it shows to a signed-in person.

    A lesson of an earlier project: after signing out on a shared laptop, Back
    showed a customer's bill again, from the browser's memory. A page the
    browser never kept cannot come back. Pages for visitors hold nothing
    private, so they are left alone.

    It reads request.user, so it runs after AuthenticationMiddleware.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.user.is_authenticated:
            add_never_cache_headers(response)
        return response
