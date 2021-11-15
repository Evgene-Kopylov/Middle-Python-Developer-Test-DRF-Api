from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status


class BookstoreApiTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()

    def test_post_publisher(self):
        data = {
            "name": "RT",
            "description": "string11"
        }
        response = self.client.post("/items/edit_publisher/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
