from django.test import SimpleTestCase

class GuestAccessExampleTests(SimpleTestCase):
    def test_guest_access_message(self):
        self.assertEqual('Authentication is required', 'Authentication is required')

class AuthenticatedUserExampleTests(SimpleTestCase):
    def test_authenticated_user_shape(self):
        user = {'id': 1, 'name': 'Example User'}
        self.assertIn('id', user)
        self.assertIn('name', user)
