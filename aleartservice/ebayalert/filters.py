import django_filters
from rest_framework import filters
from django.db import models as django_models


from ebayalert.models import AlertInfo

class EventFilter(django_filters.rest_framework.FilterSet):
    # start_date = django_filters.DateTimeFilter(field_name='alert_send_at', lookup_expr='gte')
    # end_date = django_filters.DateTimeFilter(field_name='alert_send_at', lookup_expr='lte')

    # class Meta:
    #     model = AlertInfo
    #     fields = ['alert_send_at']
    class Meta:
        model = AlertInfo
        fields = {
            'alert_send_at': ('lte', 'gte')
        }

        filter_overrides = {
            django_models.DateTimeField: {
                'filter_class': django_filters.IsoDateTimeFilter
            },
        }