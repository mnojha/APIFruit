from rest_framework import serializers
from api.models import Fruit

class FruitSerializer(serializers.ModelSerializer):

	class Meta:
		model = Fruit 
		fields = ('id', 'fruit_name')