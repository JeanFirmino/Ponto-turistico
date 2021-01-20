from .serializers import PontoTuristicoSerializer
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico

class PontoTuristicoViewSet(ModelViewSet):
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer