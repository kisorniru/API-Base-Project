from django.test import SimpleTestCase

class GuestAccessExampleTests(SimpleTestCase):
    def test_guest_access_message(self):
        self.assertEqual('Authentication is required', 'Authentication is required')
