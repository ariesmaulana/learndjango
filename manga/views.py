from rest_framework import generics
from .models import Mangas
from .serializers import MangasSerializer
# Create your views here.

class ListMangaView(generics.ListAPIView):
    """
    Provide get handler
    """

    queryset = Mangas.objects.all()
    serializer_class = MangasSerializer
