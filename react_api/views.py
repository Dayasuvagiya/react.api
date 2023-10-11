from rest_framework.decorators import api_view
from rest_framework.response import Response

# Main page view
@api_view()
def root_route(request):
    return Response({
        "message": "Welcome to my React API!"
    })