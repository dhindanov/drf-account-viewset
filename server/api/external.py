from adrf.views import APIView
from rest_framework.response import Response

from .decorators import log_api_call


async def fetch_external_account_details(account_number):
    """Simulate fetching account details from an external service."""
    # In a real implementation, this would make an HTTP request to an external API
    # For demonstration, we'll return mock data
    return {
        "account_number": account_number,
        "account_holder": "External User",
        "balance": 1000.00,
        "created_at": "2024-01-01T00:00:00Z",
        "updated_at": "2024-01-01T00:00:00Z"
    }


class ExternalBankAccountView(APIView):
    @log_api_call
    async def get(self, request, account_number):
        account_details = await fetch_external_account_details(account_number)
        return Response(account_details)
