from .models import FootbalArea
from rest_framework import viewsets
from .serializers import FootballAreaSerializer

class FootballAreaViewSet(viewsets.ModelViewSet):
    queryset = FootbalArea.objects.all()
    serializer_class = FootballAreaSerializer