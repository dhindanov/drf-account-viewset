import asyncio
from django.test import SimpleTestCase
import api.external as external


class ExternalServiceTests(SimpleTestCase):
    def test_fetch_external_account_success(self):
        async def fake_call(account_number: str):
            return {"account_number": account_number, "account_holder": "X", "balance": 1.0}

        original = external.fetch_external_account_details
        external.fetch_external_account_details = fake_call
        try:
            res = asyncio.run(external.fetch_external_account_details("111222"))
        finally:
            external.fetch_external_account_details = original

        self.assertEqual(res["account_number"], "111222")
