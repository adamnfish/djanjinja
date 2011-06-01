"""
Test utils for Djanjinja.
"""

from django.test.client import RequestFactory as DjangoRequestFactory

from djanjinja.middleware import RequestContextMiddleware


class RequestFactory(DjangoRequestFactory):
    """
    Wraps Django's RequestFactory. This class adds Djanjinja's Context
    class to the request object so that views using the
    request.Context({*}).render_* pattern can be tested using
    RequestFactories.
    """
    def request(self, *args, **kwargs):
        """
        Wrap the default request method. We'll create the WSGIRequest
        object in Django's RequestFactory and extend it here with
        Djanjinja's Context.
        """
        # TODO: only apply middleware if it appears in the settings

        # call request on parent class
        request = super(RequestFactory, self).request(*args, **kwargs)
        # mutate the request object using Djanjinja's middleware
        RequestContextMiddleware.process_request(request)
        return request
