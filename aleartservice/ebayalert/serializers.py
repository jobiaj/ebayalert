from rest_framework import serializers
from .models import *


class AlertScheduleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AlertScheduler
        fields = ('id', 'search_phrase', 'interval', 'email_address')

class AlertSerializer(serializers.ModelSerializer):
    search_phrase = serializers.ReadOnlyField(source='schedule.search_phrase', read_only=True)
    
    class Meta:
        model = AlertInfo
        fields = ('id', 'schedule', 'search_phrase', 'alert_send_at')

class ItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AlertItem
        fields = ('id', 'item_id', 'title', 'price', 'currency', 'webUrl')