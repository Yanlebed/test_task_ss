from rest_framework import serializers
from charts.models import Rate


class RateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rate
        fields = ('amount', 'date')
