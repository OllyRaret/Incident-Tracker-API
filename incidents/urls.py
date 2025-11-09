from django.urls import path
from . import views

app_name = 'incidents'

urlpatterns = [
    path(
        'incidents/',
        views.IncidentListCreateView.as_view(),
        name='incident-list-create'
    ),
    path(
        'incidents/<int:id>/',
        views.IncidentRetrieveUpdateView.as_view(),
        name='incident-detail'
    ),
]
