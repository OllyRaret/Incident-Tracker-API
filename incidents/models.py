from django.db import models
from django.utils import timezone


class IncidentStatus(models.TextChoices):
    """Статусы инцидентов"""
    OPEN = 'open', 'Открыт'
    IN_PROGRESS = 'in_progress', 'В работе'
    RESOLVED = 'resolved', 'Решен'
    CLOSED = 'closed', 'Закрыт'
    CANCELLED = 'cancelled', 'Отменен'


class IncidentSource(models.TextChoices):
    """Источники инцидентов"""
    OPERATOR = 'operator', 'Оператор'
    MONITORING = 'monitoring', 'Мониторинг'
    PARTNER = 'partner', 'Партнер'
    SYSTEM = 'system', 'Система'


class Incident(models.Model):
    """Модель инцидента"""

    description = models.TextField(
        verbose_name='Описание проблемы',
        help_text='Подробное описание инцидента'
    )

    status = models.CharField(
        max_length=20,
        choices=IncidentStatus.choices,
        default=IncidentStatus.OPEN,
        verbose_name='Статус'
    )

    source = models.CharField(
        max_length=20,
        choices=IncidentSource.choices,
        verbose_name='Источник'
    )

    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name='Время создания'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Время последнего обновления'
    )

    class Meta:
        verbose_name = 'Инцидент'
        verbose_name_plural = 'Инциденты'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['status']),
            models.Index(fields=['source']),
            models.Index(fields=['created_at']),
        ]

    def __str__(self):
        return f'Инцидент #{self.id} - {self.get_status_display()}'
