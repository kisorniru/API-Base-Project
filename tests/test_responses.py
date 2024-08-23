from django.test import SimpleTestCase

from apps.core.responses import build_response

class ResponseHelperTests(SimpleTestCase):
    def test_build_response_marks_success(self):
        response = build_response({'ok': True})
        self.assertTrue(response.data['success'])
        self.assertEqual(response.data['data'], {'ok': True})
