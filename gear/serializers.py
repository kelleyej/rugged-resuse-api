from rest_framework import serializers
from .models import Gear

class GearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gear
        fields = ['id', 'title', 'description', 'image', 'category']