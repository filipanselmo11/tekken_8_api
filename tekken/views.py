from rest_framework import viewsets, filters
from tekken.serializers import TekkenSerializer
from tekken.models import Tekken
from django_filters.rest_framework import DjangoFilterBackend

class TekkenViewSet(viewsets.ModelViewSet):
    """Listando os lutadores"""
    queryset = Tekken.objects.all()
    serializer_class = TekkenSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_filters = ['nome']
    search_fields = ['nome', 'nacionalidade']
    filterset_fields = ['nacionalidade']