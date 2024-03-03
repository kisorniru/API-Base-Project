from rest_framework.response import Response

def build_response(data=None, message='OK', status_code=200):
    return Response({
        'success': status_code < 400,
        'message': message,
        'data': data,
    }, status=status_code)

def success_response(data=None, message='Request completed', status_code=200):
    return build_response(data=data, message=message, status_code=status_code)
