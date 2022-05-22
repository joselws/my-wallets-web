from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from models import Wallet

class WalletTestCase(TestCase):
    """Test the wallet model"""

    def setUp(self):
        """User models used in each test"""
        self.test_user = User.objects.create_user(
                            username='test', 
                            password='pass123', 
                            email='test@user.com'
                        )
        
        
    def test_wallet_correctly_created(self):
        """Test wallet was correctly created"""
        test_wallet = Wallet.objects.all(
                        user=self.test_user
                        name='test', 
                        balance=2500,
                        percent=80,
                        cap=50000
                        )
        self.assertEqual(Wallet.objects.all().count(), 1)
        self.assertEqual(test_wallet.user.username, 'test')
        self.assertEqual(test_wallet.name, 'test')
        self.assertEqual(test_wallet.balance, 2500)
        self.assertEqual(test_wallet.percent, 80)
        self.assertEqual(test_wallet.cap, 50000)

    def test_wallet_default_values_correctly_created(self):
        """Test wallet with default values correctly created"""
        test_wallet = Wallet.objects.all(user=self.test_user, name='test')
        self.assertEqual(Wallet.objects.all().count(), 1)
        self.assertEqual(test_wallet.user.username, 'test')
        self.assertEqual(test_wallet.name, 'test')
        self.assertEqual(test_wallet.balance, 0)
        self.assertEqual(test_wallet.percent, 0)
        self.assertEqual(test_wallet.cap, 0)

    def test_no_negative_percent(self):
        """Percent values must be at least 0"""
        with self.assertRaises(IntegrityError):
            Wallet.objects.create(user=self.test_user, name='test', percent=-50)
        self.assertQuerysetEqual(Wallet.objects.all().count(), 0)

    def test_no_percent_above_100(self):
        """Percent max value is 100"""
        with self.assertRaises(ValidationError):
            Wallet.objects.create(user=self.test_user, name='test', percent=150)
        self.assertQuerysetEqual(Wallet.objects.all().count(), 0)

    def test_no_negative_percent(self):
        """Percent values must be at least 0"""
        with self.assertRaises(IntegrityError):
            Wallet.objects.create(user=self.test_user, name='test', cap=-50)
        self.assertQuerysetEqual(Wallet.objects.all().count(), 0)