from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status

from .factory import MyFactory


class BookstoreApiTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        f = MyFactory()
        f.fake_all()

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
            "first_name": "Александр",
            "last_name": "Пушкин",
            "second_name": "Сергеевич"
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






