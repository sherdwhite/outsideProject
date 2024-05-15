from datetime import datetime
from dateutil.parser import parse
import re

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Picture
from .nasa_api import fetch_nasa_apod
from .serializers import PictureSerializer
from .wiki_api import get_wikipedia_summary


class PictureAPIView(APIView):
    def get(self, request):
        date = request.GET.get("date")

        try:
            # If date is not provided, default to today's date
            date = (
                datetime.today().strftime("%Y-%m-%d")
                if not date
                else parse(date).strftime("%Y-%m-%d")
            )
        except ValueError:
            return Response(
                {"error": "Invalid date format. Date should be in YYYY-MM-DD format."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            data = fetch_nasa_apod(date)
        except ConnectionError:
            return Response(
                {"error": "Failed to retrieve data from NASA API."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not data:
            return Response(
                {"error": "Failed to retrieve data from NASA API."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        additional_data = get_wikipedia_summary(data.get("explanation", ""))

        picture, created = Picture.objects.update_or_create(
            date=data["date"],
            title=data.get("title", ""),
            url=data.get("url", ""),
            hdurl=data.get("hdurl", ""),
            explanation=data.get("explanation", ""),
            media_type=data.get("media_type", ""),
            service_version=data.get("service_version", ""),
            copyright=data.get("copyright", ""),
            additional_data=additional_data,
        )

        serializer = PictureSerializer(picture)

        return Response(serializer.data, status=status.HTTP_200_OK)
