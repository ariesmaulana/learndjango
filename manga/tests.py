from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Mangas
from .serializers import MangasSerializer

# Create your tests here.

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_manga(title='', author=''):
        if title !='' and author !='':
            Mangas.objects.create(title=title, author=author)

    def setUp(self):
        self.create_manga('Naruto','Kishimoto')
        self.create_manga('One Piece','Eichiro Oda')
        self.create_manga('Bleach','Tite Kubo')

class GetAllMangaTest(BaseViewTest):
    
    def test_get_all_manga(self):
        """
        This test ensures that all mangas added in the setup method
        exist when we make get request to the manga endpoint
        """

        response = self.client.get(
            reverse('manga-all', kwargs={"version": "v1"})
        )

        expected = Mangas.objects.all()
        serialized = MangasSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
