from rest_framework import serializers
from .models import Records
from . import models
import datetime

class RecordsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Education
        fields = ('id', 'event_dateTime', 'event_agenda', 'user')

     def create(self, validated_data):

        # Save request
        request = models.Request(
            event_=validated_data["desc"],
            date_need=validated_data["date_need"],
            date_borrow=validated_data["date_borrow"],
            community=validated_data["community"],
            requester=validated_data["requester"],
        )

        request.save()
