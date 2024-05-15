from django.urls import path
from .views import PictureAPIView

# Since I used the class-based view PictureAPIView, I didn't use the routers to register the view.
# I would probably update this to use viewsets and routers if I was going to expand the API.
urlpatterns = [
    path('picture/', PictureAPIView.as_view(), name='picture'),
]