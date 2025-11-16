from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def login_view(request):
    return Response({'message': 'Login successful'})

@api_view(['GET'])
def register_view(request):
    return Response({'message': 'Register successful'})

@api_view(['GET'])
def logout_view(request):
    return Response({'message': 'Logout successful'})
