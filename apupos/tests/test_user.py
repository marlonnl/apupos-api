from django.test import TestCase
from django.contrib.auth.models import User


class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test_user", password="test_user")

    def test_user_created(self):
        self.assertEqual(self.user.username, "test_user")
