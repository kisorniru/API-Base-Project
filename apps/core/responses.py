from rest_framework.response import Response

def build_response(data=None, message='OK', status_code=200):
    return Response({
        'success': status_code < 400,
        'message': message,
        'data': data,
    }, status=status_code)

def success_response(data=None, message='Request completed', status_code=200):
    return build_response(data=data, message=message, status_code=status_code)

def error_response(message='Request failed', errors=None, status_code=400):
    return Response({
        'success': False,
        'message': message,
        'errors': errors or {},
    }, status=status_code)

def validation_error_response(errors, message='Validation failed'):
    return error_response(message=message, errors=errors, status_code=422)

def not_found_response(message='Resource not found'):
    return error_response(message=message, errors={'code': 'not_found'}, status_code=404)
