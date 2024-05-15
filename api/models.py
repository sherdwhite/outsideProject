from ast import Dict
from django.db import models


# Model for the astronomy picture of the day from api.nasa.gov
class Picture(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=100)
    explanation = models.TextField()
    url = models.URLField()
    hdurl = models.URLField()
    media_type = models.CharField(max_length=10)
    service_version = models.CharField(max_length=10)
    copyright = models.CharField(max_length=100)
    additional_data = models.CharField(max_length=400, blank=True, null=True)

    def __str__(self):
        return self.title
