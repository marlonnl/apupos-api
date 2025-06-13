from django.test import TestCase
from django.contrib.auth.models import User


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username="test_user", password="test_user")

    def test_user_created(self):
        user = User.objects.get(username="test_user")
        self.assertEqual(user.username, "test_user")
