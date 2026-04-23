from django.test import TestCase
from api.models import BankAccount
from api.serializers import BankAccountSerializer


class BankAccountSerializerTests(TestCase):
    def test_serialize_model(self):
        acct = BankAccount.objects.create(
            account_number="ACC456", account_holder="Bob", balance=50.0
        )
        data = BankAccountSerializer(acct).data
        self.assertEqual(data["account_number"], "ACC456")
        self.assertEqual(data["account_holder"], "Bob")
        self.assertIn("balance", data)

    def test_validate_and_save_input(self):
        data = {"account_number": "ACC789", "account_holder": "Carol", "balance": "75.5"}
        serializer = BankAccountSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        obj = serializer.save()
        self.assertEqual(obj.account_number, "ACC789")
        self.assertEqual(obj.account_holder, "Carol")
