from django.test import TestCase
from users.models import Users


class UserTestCase(TestCase):

    def create_user(self, name="John Doe", email="john@email.com", login="john", password="123456"):
        return Users.objects.create(name=name, email=email, login=login, password=password) 

    def test_user_creation(self):
        p1 = self.create_user()
        self.assertTrue(isinstance(p1, Users))
        self.assertEqual(p1.__str__(), p1.name, p1.email)

