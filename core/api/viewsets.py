from pip._vendor.certifi.__main__ import args
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import PontoTuristicoSerializer
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico


class PontoTuristicoViewSet(ModelViewSet):
    #queryset = PontoTuristico.objects.all(aprovado=True)

    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

    def list(self, request, *arg, **kwargs):
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    def retrice(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrice(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

    @action(methods=['get'], detail=True)
    def denunciar(self, request, pk=None):
        return

    @action(methods=['get'], detail=False)
    def teste(self, request):
        pass
