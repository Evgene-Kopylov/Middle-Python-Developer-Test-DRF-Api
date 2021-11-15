from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status

from .factory import MyFactory

from .models import Book

class BookstoreApiTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        f = MyFactory()
        f.fake_it(5)

    def test_get_publisher(self):
        response = self.client.get("/items/edit_publisher/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_author(self):
        response = self.client.get("/items/edit_author/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_book(self):
        response = self.client.get("/items/edit_book/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_post_publisher(self):
        data = {
            "name": "RT",
            "description": "string11"
        }

        response = self.client.post("/items/edit_publisher/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_author(self):
        data = {
            "first_name": "Алекс",
            "last_name": "Егого",
            "second_name": "Серг"
        }

        response = self.client.post("/items/edit_author/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_book(self):
        data = {
            "title": "Книга ЩЩФЗ",
            "annotation": "загадочная",
            "isbn": "123456789123",
            "publish_at": "2021-11-15",
            "total_sells": 0,
            "total_views": 0,
            "authors": [
                1
            ],
            "publisher": 1
        }

        response = self.client.post("/items/edit_book/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_patch_publisher(self):
        data = {
            "name": "RT",
            "description": "oppa ono to"
        }
        response = self.client.patch("/items/edit_publisher/1/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_author(self):
        data = {
            "first_name": "Александр",
            "last_name": "Пушкин",
            "second_name": "Сергеевич",
        }
        response = self.client.patch("/items/edit_author/1/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_book(self):
        data = {
            "title": "Book title",
            "annotation": "Book annotation...",
        }
        response = self.client.patch("/items/edit_book/1/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_publisher(self):
        response = self.client.delete("/items/edit_publisher/1/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_author(self):
        response = self.client.delete("/items/edit_author/1/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_book(self):
        response = self.client.delete("/items/edit_book/1/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

