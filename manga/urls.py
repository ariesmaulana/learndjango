from django.urls import path
from .views import ListMangaView

urlpatterns = [
    path('manga/', ListMangaView.as_view(), name='manga-all')
]