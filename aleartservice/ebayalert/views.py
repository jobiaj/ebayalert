import django_filters.rest_framework
from rest_framework import viewsets

from .serializers import *
from .models import *
from .filters import *


class AlertScheduleView(viewsets.ModelViewSet):
    serializer_class = AlertScheduleSerializer
    queryset = AlertScheduler.objects.all()

class AlertView(viewsets.ReadOnlyModelViewSet):
    serializer_class = AlertSerializer
    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    # filterset_fields = {'alert_send_at': ['gte', 'lte', 'exact', 'gt', 'lt']}
    filter_class = EventFilter

    def get_queryset(self):
       return AlertInfo.objects.filter(schedule=self.kwargs.get('schedule_id')).order_by('-alert_send_at')

class AlertItemView(viewsets.ReadOnlyModelViewSet):
    serializer_class = ItemSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['price', 'title']

    def get_queryset(self):
       alert_info = AlertInfo.objects.get(id=self.kwargs.get('alert_id'))
       return alert_info.items.all().order_by('price')