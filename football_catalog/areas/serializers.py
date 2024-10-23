from rest_framework import serializers
from .models import FootbalArea


class FootballAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FootbalArea
        fields = '__all__'