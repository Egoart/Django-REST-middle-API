from .models import Album
from .serializers import AlbumSerializer

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

# Create your tests here.


class AlbumTesting(APITestCase):
    def setUp(self) -> None:
        Album.objects.create(userId=1, id=1, title="FirstAlbum")
        Album.objects.create(userId=1, id=2, title="SecondAlbum")
        Album.objects.create(userId=1, id=3, title="ThirdAlbum")

        return super().setUp()

    def test_album_get_response(self):
        response = self.client.get(reverse("albums"))
        albums = Album.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
