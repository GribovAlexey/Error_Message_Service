import logging
from time import timezone


logger = logging.getLogger(__name__)


class RequestTimeLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.info(f'Request start at {timezone.now()}')
        return self.get_response(request)
