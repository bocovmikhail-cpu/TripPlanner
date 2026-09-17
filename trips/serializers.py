from rest_framework import serializers
from .models import Trip


class TripSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.id")

    class Meta:
        model = Trip
        fields = ["id", "title", "destination", "start_date", "end_date", "owner"]
