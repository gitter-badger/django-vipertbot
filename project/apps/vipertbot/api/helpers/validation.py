from rest_framework import status
from rest_framework.exceptions import APIException
from django.utils.encoding import force_text

class ApiValidationError(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = 'A server error occurred.'

    def __init__(self, detail):
        if detail is not None:
            self.detail = {'error': force_text(detail)}
        else:
            self.detail = {'error': force_text(self.default_detail)}