from rest_framework.response import Response

def api_response(data=None, message='OK', status_code=200):
    return Response({
        'success': status_code < 400,
        'message': message,
        'data': data,
    }, status=status_code)
