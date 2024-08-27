from django.test import SimpleTestCase

from apps.core.responses import build_response

class ResponseHelperTests(SimpleTestCase):
    def test_build_response_marks_success(self):
        response = build_response({'ok': True})
        self.assertTrue(response.data['success'])
        self.assertEqual(response.data['data'], {'ok': True})

from apps.core.responses import validation_error_response

class ValidationResponseTests(SimpleTestCase):
    def test_validation_response_uses_422(self):
        response = validation_error_response({'email': ['Required']})
        self.assertEqual(response.status_code, 422)
        self.assertFalse(response.data['success'])
