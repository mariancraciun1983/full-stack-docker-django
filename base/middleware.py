class SetRemoteAddrMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        # should I use get_response?
        if 'HTTP_X_REAL_IP' in request.META and request.META['HTTP_X_REAL_IP']:
            request.META["REMOTE_ADDR"] = request.META["HTTP_X_REAL_IP"]

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
