from api.validators import validate_100_max
from django.core.exceptions import ValidationError
from django.test import SimpleTestCase

class TestValidate100Max(SimpleTestCase):
    """Test this validator functionality"""

    def test_valid_values(self):
        """Return input value if below 100"""
        self.assertEqual(validate_100_max(0), 0)
        self.assertEqual(validate_100_max(50), 50)
        self.assertEqual(validate_100_max(100), 100)

    def test_invalid_value_over_100(self):
        """Values over 100 raises the ValidationError exception"""
        with self.assertRaises(ValidationError):
            validate_100_max(101)