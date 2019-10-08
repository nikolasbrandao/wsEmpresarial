from ..models import Produto
from . import serializers
from rest_framework import generics, status
from rest_framework.response import Response

class ProdutoListView(generics.ListAPIView):
    queryset = Produto.objects.all()
    serializer_class = serializers.ProdutoSerializer

