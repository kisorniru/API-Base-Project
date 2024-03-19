from rest_framework.decorators import api_view
from apps.core.responses import success_response

@api_view(['GET'])
def health_check(request):
    return success_response({'status': 'ok'}, message='API is healthy')

@api_view(['POST'])
def echo(request):
    from apps.api.serializers import EchoSerializer
    from apps.core.responses import validation_error_response

    serializer = EchoSerializer(data=request.data)
    if not serializer.is_valid():
        return validation_error_response(serializer.errors)
    return success_response(serializer.validated_data, message='Echo accepted')
