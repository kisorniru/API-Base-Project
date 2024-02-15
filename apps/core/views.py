from rest_framework.views import APIView

class BaseAPIView(APIView):
    """Small base class for shared API view behavior."""

    authentication_classes = []
    permission_classes = []
