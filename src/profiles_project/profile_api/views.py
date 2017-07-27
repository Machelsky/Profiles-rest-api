from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication

from . import serializers
from . import models
from . import permissions
# Create your views here.

class HelloApiView(APIView):
	"""Test API View."""
	serializer_class = serializers.HelloSerializer

	def get(self, request, format= None):
		"""Returns a list of APIView features."""

		an_apiview = [
			'Uses HTTP methods as function(get, post, patch, put, delete',
			'2lol',
			'3eeg',
			'4eeer'
		]

		return Response({'message':'Hello','an_apiview': an_apiview})


	def post(self, request):
		"""Create a hello message with our name."""

		serializer = serializers.HelloSerializer(data = request.data)

		if serializer.is_valid():
			name = serializer.data.get('name')
			message = 'hello {0}'.format(name)
			return Response({'message':message})
		else:
			return Response(serializer.erros, status = status.HTTP_400_BAD_REQUEST)

	def put(self, request, pk=None):
		"""Handles updating an object."""

		return Response({'method':'put'})

	def patch(self, request, pk=None):
		"""Path request, only updates fields provided in the request."""

		return Response({'method':'patch'})

	def delete(self, request, pk=None):
		return Response({'method':'delete'})


class HelloViewSet(viewsets.ViewSet):
	"""Test API ViewSet"""

	serializer_class = serializers.HelloSerializer

	def list(self, request):
		"""Return a Hello message"""

		a_viewset = [
			"Use actions(list, create, retrieve, update, partial_update)",
			"Automatically maps to URLS with routers",
			"Provides more funcationality with less code"
		]
		return Response({'message':'hello','a_viewset':a_viewset})

	def create(self, request):
		"""create a new hello message."""

		serializer = serializers.HelloSerializer(data=request.data)

		if serializer.is_valid():
			name = serializer.data.get('name')
			message = 'hello {0}'.format(name)
			return Response({'message':message})
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def retrieve(self, request, pk=None):
		"""Handles getting an object by its ID."""

		return Response({'http_method':'GET'})

	def update(self, request, pk=None):
		"""Handles updating an object."""

		return Response({'http_method':'PUI'})

	def partial_update(self, request, pk=None):
		"""handles updating part of an object"""

		return Response({'http_method':'patch'})

	def destroy(self, request, pk=None):
		"""handles destroying object"""
		return Response({'http_method':'destroy'})


class UserProfileViewSet(viewsets.ModelViewSet):
	"""Handles creating, creating and updating profiles."""

	serializer_class = serializers.UserProfileSerializer
	queryset = models.UserProfile.objects.all()
	authentication_classes = (TokenAuthentication,)
	permission_classes = (permissions.UpdateOwnProfile,)

