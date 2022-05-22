from django.test import TestCase
from models import User

class UserTestCase(TestCase):
    """Test the user model"""

    def setUp(self):
        """User models used in each test"""
        self.test_user = User.objects.create_user (
                            username='test', 
                            password='pass123', 
                            email='test@user.com'
                        )
        
    def test_user_correctly_created(self):
        """Test the user in setUp was correctly created"""
        self.assertQuerysetEqual(User.objects.all().count(), 1)
        self.assertEqual(self.test_user.username, 'test')
        self.assertEqual(self.test_user.email, 'test@user.com')

    def test_no_duplicate_username(self):
        """Usernames must be unique among all users"""
        with self.assertRaises(IntegrityError):
            test_user2 = User.objects.create_user('test', 'pass123', 'another@user.com')
        self.assertQuerysetEqual(User.objects.all().count(), 1)

    def test_no_duplicate_email(self):
        """emails must be unique among all users"""
        with self.assertRaises(IntegrityError):
            test_user2 = User.objects.create_user('another_user', 'pass123', 'test@user.com')
        self.assertQuerysetEqual(User.objects.all().count(), 1)

    # I could keep testing further the max_length value of username and email,
    # but these features are already thoroughly tested by django.
    # these tests were mostly added for a bit of additional coverage