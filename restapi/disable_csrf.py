from django.utils.deprecation import MiddlewareMixin
import logging

logging.basicConfig(encoding='utf-8', level=logging.DEBUG)

class DisableCSRF(MiddlewareMixin):
    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)
        # We could log after the function with the action/task it has completed
        # Not sure what the function does 
        logging.info("[DisableCSRF]: Request is processed.")