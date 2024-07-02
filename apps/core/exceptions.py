from rest_framework.views import exception_handler

from apps.core.responses import error_response, validation_error_response

def api_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is None:
        return error_response('Unexpected server error', status_code=500)
    if response.status_code == 400:
        return validation_error_response(response.data)
    return error_response(str(getattr(exc, 'detail', 'Request failed')), status_code=response.status_code)
