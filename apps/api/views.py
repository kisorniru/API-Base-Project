from rest_framework.decorators import api_view
from apps.core.responses import success_response

@api_view(['GET'])
def health_check(request):
    return success_response({'status': 'ok'}, message='API is healthy')
