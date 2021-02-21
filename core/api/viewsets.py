from pip._vendor.certifi.__main__ import args
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser, DjangoModelPermissions
from rest_framework.response import Response
from .serializers import PontoTuristicoSerializer
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico


class PontoTuristicoViewSet(ModelViewSet):
    #queryset = PontoTuristico.objects.all(aprovado=True)

    serializer_class = PontoTuristicoSerializer
    #permission_classes = (IsAuthenticated)
    authentication_classes = (TokenAuthentication)
    #permission_classes = (IsAdminUser)
    permission_classes = (DjangoModelPermissions)

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        if id:
            queryset = PontoTuristico.objects.filter(pk=id)
        if nome:
            queryset = queryset.filter(nome=nome)
        if descricao:
            queryset = queryset.filter(descricao=descricao)
        return queryset

#return PontoTuristico.objects.filter(aprovado=True)

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

    filter_backends = (SearchFilter)
    search_fields = ('nome','descricao','endereco__linha1')
    lookup_field = 'nome'
