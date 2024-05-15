from rest_framework import serializers
from .models import Picture


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = (
            "date",
            "title",
            "explanation",
            "url",
            "hdurl",
            "media_type",
            "service_version",
            "copyright",
            "additional_data",
        )
