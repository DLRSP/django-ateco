"""Tests for django-ateco adapters."""

from django.test import SimpleTestCase

from django_ateco import services


class AtecoServicesTests(SimpleTestCase):
    def test_validate_known_code(self):
        self.assertTrue(services.validate("01.11.00"))
        self.assertTrue(services.validate("552042"))

    def test_lookup_default_edition(self):
        node = services.lookup("01.11.00")
        self.assertIsNotNone(node)
        self.assertEqual(node.edition, "2025")

    def test_editions_include_2025(self):
        keys = {e.key for e in services.editions()}
        self.assertIn("2025", keys)
