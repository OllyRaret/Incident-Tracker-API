from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from .models import Incident
from .serializers import (
    IncidentSerializer,
    IncidentCreateSerializer,
    IncidentUpdateSerializer
)


class IncidentListCreateView(generics.ListCreateAPIView):
    """
    API endpoint для получения списка инцидентов и создания новых
    """
    queryset = Incident.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['status', 'source']
    ordering_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return IncidentCreateSerializer
        return IncidentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        incident = serializer.save()

        # Возвращаем полный объект после создания
        full_serializer = IncidentSerializer(incident)
        return Response(full_serializer.data, status=status.HTTP_201_CREATED)


class IncidentRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    """
    API endpoint для получения и обновления инцидента по ID
    Обновление разрешено только для статуса
    """
    queryset = Incident.objects.all()
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return IncidentUpdateSerializer
        return IncidentSerializer

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except Incident.DoesNotExist:
            raise NotFound(detail="Инцидент не найден")
