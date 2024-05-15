from django.test import TestCase, RequestFactory
from unittest.mock import patch
from rest_framework import status

from .views import PictureAPIView

class TestPictureAPIView(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.view = PictureAPIView.as_view()

    @patch('api.views.fetch_nasa_apod')
    @patch('api.views.get_wikipedia_summary')
    def test_get_with_valid_date(self, mock_get_wikipedia_summary, mock_fetch_nasa_apod):
        mock_fetch_nasa_apod.return_value = {
            "date": "2024-01-01",
            "title": "Test Title",
            "url": "http://testurl.com",
            "hdurl": "http://testhdurl.com",
            "explanation": "Test Explanation",
            "media_type": "image",
            "service_version": "v1",
            "copyright": "Test Copyright"
        }
        mock_get_wikipedia_summary.return_value = "Test Summary"

        request = self.factory.get('/api/picture/', {'date': '2024-01-01'})
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @patch('api.views.fetch_nasa_apod')
    def test_get_with_invalid_date(self, mock_fetch_nasa_apod):
        mock_fetch_nasa_apod.return_value = None

        request = self.factory.get('/api/picture/', {'date': 'invalid-date'})
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @patch('api.views.fetch_nasa_apod')
    @patch('api.views.get_wikipedia_summary')
    def test_get_without_date(self, mock_get_wikipedia_summary, mock_fetch_nasa_apod):
        mock_fetch_nasa_apod.return_value = {
            "date": "2024-01-01",
            "title": "Test Title",
            "url": "http://testurl.com",
            "hdurl": "http://testhdurl.com",
            "explanation": "Test Explanation",
            "media_type": "image",
            "service_version": "v1",
            "copyright": "Test Copyright"
        }
        mock_get_wikipedia_summary.return_value = "Test Summary"

        request = self.factory.get('/api/picture/')
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @patch('api.views.fetch_nasa_apod')
    def test_get_with_failed_nasa_api(self, mock_fetch_nasa_apod):
        mock_fetch_nasa_apod.return_value = None

        request = self.factory.get('/api/picture/', {'date': '2024-01-01'})
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)