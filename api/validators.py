from django.core.exceptions import ValidationError

def validate_100_max(value):
    """Raises exception if we pass a value greater than 100"""
    if value > 100:
        raise ValidationError('Maximum value must be 100')
    return value