from rest_framework.views import APIView
from rest_framework.response import Response

class HelloAPIView(APIView):
    """Test API View"""

    def get(self, request, format= None):
        '''Returns a list of API View features'''

        an_apiview = [
            'Apple',
            'Banana',
            'Orange', 
            'Pear'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})