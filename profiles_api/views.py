#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import models
from profiles_api import permissions

# Create your views here.
class HelloApiView(APIView):
    """Test API view"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format = None):
        """Returns a list of API features"""
        an_apiview = [
            'Uses HTTP methods as functions (get, post, put, patch, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """create a hello message with our name"""
        serializer= self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            place = serializer.validated_data.get('place')
            message = f'Hello {name} from {place}'
            return Response({'message': message})
        else:
            return Response(
            serializer.errors ,
            status = status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk =None):
        """Handles updating an object"""
        return Response({'method':'PUT'})

    def patch(self, request, pk =None):
        """Handles a partial update of an object"""
        return Respone({'method':'PATCH'})

    def delete(self, request, pk =None):
        """Deletes an object"""
        return Response({'method':'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test API view set"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            'Uses actions (List, create, retrieve, update, partial update)',
            'Automatically maps to urls using routers',
            'Provides more functionality with less code'
        ]

        return Response({'message':'Hello' , 'a_viewset':a_viewset})

    def create(self, request):
        """create a new hello message"""
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello ! {name}'
            return Response({'message': message})
        else :
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk = None):
        """Handles getting an object by id"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk = None):
        """Handles updating an object"""
        return Response({'http_method' : 'PUT'})

    def partial_update(self, request, pk = None):
        """Handles updating part of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk = None):
        """Handles removing an object"""
        return Response({'http_method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating user profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
