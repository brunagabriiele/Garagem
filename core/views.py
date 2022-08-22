from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from core.models import Categoria, Carro, Marca
from core.serializers import CategoriaSerializer, MarcaSerializer, CarroSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return CategoriaDetailSerializer
        return CategoriaSerializer


class CarroViewSet(ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer
def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return CarroDetailSerializer
        return CarroSerializer

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return MarcaDetailSerializer
        return MarcaSerializer

   
