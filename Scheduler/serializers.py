from .models import Activity, Table
from rest_framework import serializers

# Serializers define the API representation.
class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'text', 'day', 'time', 'table_id']

class TableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Table
        fields = ['id', 'name']