from django.shortcuts import render
from django.http import JsonResponse
from  . import models

from rest_framework import generics
from .serializers import FruitSerializer
from .models import Fruit

class CreateView(generics.ListCreateAPIView):
	queryset = Fruit.objects.all()
	serializer_class = FruitSerializer

	def perform_create(self, serializer):
			serializer.save()	