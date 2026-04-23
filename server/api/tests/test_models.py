from django.test import TestCase
from api.models import BankAccount


class BankAccountModelTests(TestCase):
    def test_create_account(self):
        acct = BankAccount.objects.create(
            account_number="ACC123", account_holder="Alice", balance=123.45
        )
        self.assertEqual(acct.account_number, "ACC123")
        self.assertEqual(acct.account_holder, "Alice")
        self.assertEqual(float(acct.balance), 123.45)
        self.assertIsNotNone(acct.pk)
