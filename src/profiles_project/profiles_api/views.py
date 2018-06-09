from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as function (get, post, pathc, put, delete)',
            'It is similar to a tranditional Django view',
            'Gives you the most conrol ovber your logic',
            'Is mapped manualy to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
