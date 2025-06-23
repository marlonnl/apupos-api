from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient


from ..models.apupo import Apupo


class APIEndpointsTestCase(TestCase):
    def setUp(self):
        # usuarios
        self.user = User.objects.create_user(username="test_user", password="test_user")

        # criando uma postagem para testagem
        Apupo.objects.create(user=self.user, content="post test")

    def get_client(self):
        client = APIClient()
        client.login(username=self.user.username, password="test_user")
        return client

    def test_apupo_list(self):
        """
        Verifica o endpoint APUPO
        Status code 200
        response: [posts]
        """
        client = self.get_client()
        response = client.get("/api/apupo/")

        self.assertEqual(response.status_code, 200)  # status code
        self.assertEqual(len(response.json()), 1)  # 1 post
        # [{'id': 1, 'content': 'post test', 'likes': 0, 'is_retweet': False, 'parent': None}]

    def test_apupo_created(self):
        """
        Verificar a criação de postagem
        """
        apupo = Apupo.objects.create(content="test", user=self.user)

        self.assertEqual(apupo.id, 2)  # segunda postagem, id 2
        self.assertEqual(apupo.user, self.user)  # usuário
        self.assertEqual(apupo.content, "test")  # conteudo

    def test_action_like(self):
        client = self.get_client()
        response = client.post("/api/apupo/action/", {"id": 1, "action": "like"})
        likes = response.json().get("likes")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(likes, 1)

    def test_action_unlike(self):
        client = self.get_client()
        response = client.post("/api/apupo/action/", {"id": 1, "action": "like"})
        self.assertEqual(response.status_code, 200)

        response = client.post("/api/apupo/action/", {"id": 1, "action": "unlike"})
        self.assertEqual(response.status_code, 200)
        likes = response.json().get("likes")

        self.assertEqual(likes, 0)
