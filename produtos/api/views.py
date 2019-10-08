from ..models import Produto
from . import serializers
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework_xml.renderers import XMLRenderer

class ProdutoListView(generics.ListAPIView):
    renderer_classes = (JSONRenderer, XMLRenderer)
    queryset = Produto.objects.all()
    serializer_class = serializers.ProdutoSerializer

