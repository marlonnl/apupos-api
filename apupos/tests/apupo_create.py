# from django.test import TestCase
# from django.contrib.auth.models import User

# from ..models.apupo import Apupo


# class CreateApupoTestCase(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username="test_user", password="test_user")

#     def test_apupo_created(self):
#         apupo = Apupo.objects.create(content="test", user=self.user)
#         self.assertEqual(apupo.id, 1)
#         self.assertEqual(apupo.user, self.user)
