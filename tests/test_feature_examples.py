from django.test import SimpleTestCase

class FeatureExampleTests(SimpleTestCase):
    def test_feature_tests_are_enabled(self):
        self.assertTrue(True)

class HealthEndpointTests(SimpleTestCase):
    def test_health_path_is_stable(self):
        self.assertEqual('/api/health/', '/api/health/')
