from rest_framework import serializers
from .models import Records
from . import models
import datetime

class RecordsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Records
        fields = ('id', 'event_date', 'event_agenda', 'user')

    def create(self, validated_data):
        if validated_data["event_date"] < datetime.date.today():
            print(validated_data["event_date"])
            raise ValueError("Date must be higher than current date time")
        # Save request
        record = models.Records(
        event_date=validated_data["event_date"],
        event_agenda=validated_data["event_agenda"],
        user=validated_data["user"]
        )

        record.save()
        return record
