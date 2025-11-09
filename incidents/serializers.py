from rest_framework import serializers
from .models import Incident, IncidentStatus, IncidentSource


class IncidentSerializer(serializers.ModelSerializer):
    """Сериализатор для инцидентов"""

    status_display = serializers.CharField(
        source='get_status_display',
        read_only=True
    )
    source_display = serializers.CharField(
        source='get_source_display',
        read_only=True
    )

    class Meta:
        model = Incident
        fields = [
            'id',
            'description',
            'status',
            'status_display',
            'source',
            'source_display',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class IncidentCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания инцидентов"""

    class Meta:
        model = Incident
        fields = ['description', 'source']

    def validate_source(self, value):
        """Валидация источника"""
        if value not in IncidentSource.values:
            raise serializers.ValidationError(
                f"Недопустимый источник. Допустимые значения: {', '.join(IncidentSource.values)}"
            )
        return value


class IncidentUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор для обновления статуса инцидента"""

    class Meta:
        model = Incident
        fields = ['status']

    def validate_status(self, value):
        """Валидация статуса"""
        if value not in IncidentStatus.values:
            raise serializers.ValidationError(
                f"Недопустимый статус. Допустимые значения: {', '.join(IncidentStatus.values)}"
            )
        return value
