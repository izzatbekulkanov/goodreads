from django.contrib.auth import get_user
from django.test import TestCase
from users.models import CustomUser
from django.urls import reverse

# Create your tests here.
class RegistrationTestCase(TestCase):
    def test_user_account_is_created(self):
        self.client.post(
            reverse("users:register"),
                         data={"username":"auzcoder",
                               "first_name":"Abdulhafiz",
                               "last_name":"Davlatov",
                               "email":"auz.offical@gmail.com",
                               "password":"somepassword"
                               }
                         )

        user = CustomUser.objects.get(username="auzcoder")

        self.assertEqual(user.first_name, "Abdulhafiz")
        self.assertEqual(user.last_name, "Davlatov")
        self.assertEqual(user.email, "auz.offical@gmail.com")
        self.assertNotEqual(user.password, "somepassword")
        self.assertTrue(user.check_password("somepassword"))

    def test_required_fields(self):
        response = self.client.post(
            reverse('users:register'),
            data={
                "first_name":"Abdulhafiz",
                "email":"auz.offical@gmail.com"
            }
        )

        user_count = CustomUser.objects.count()

        self.assertEqual(user_count, 0)
        self.assertFormError(response, "form", "username", "This fields is required.")
        self.assertFormError(response, "form", "password", "This fields is required.")

    def test_invalid_email(self):
        response = self.client.post(
            reverse("users:register"),
            data={"username": "auzcoder",
                  "first_name": "Abdulhafiz",
                  "last_name": "Davlatov",
                  "email": "textemail",
                  "password": "somepassword"
                  }
        )

        user_count = CustomUser.objects.count()

        self.assertEqual(user_count, 0)
        self.assertFormError(response, "form", "email", "Enter a valid email address.")

    def test_unique_username(self):
        pass

class LoginTestCase(TestCase):
    def test_successful_login(self):
        db_user = CustomUser.objects.create(username='admin', first_name='Abdulhafiz')
        db_user.set_password('somepass')
        db_user.save()

        self.client.post(
            reverse('users:login'),
            data={
                'usernsme':'admin',
                'password':'somepass'
            }
        )

        user = get_user(self.client)

        self.assertTrue(user.is_authenticated)

    def test_wrong_credentials(self):
        db_user = CustomUser.objects.create(username='admin', first_name='Abdulhafiz')
        db_user.set_password('somepass')
        db_user.save()

        self.client.post(
            reverse('users:login'),
            data={
                'usernsme': 'webadmin',
                'password': 'somepass'
            }
        )
        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)

        self.client.post(
            reverse('users:login'),
            data={
                'usernsme': 'admin',
                'password': 'somepassword'
            }
        )
        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)

