import structlog
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response

from .decorators import log_api_viewset, log_api_call
from .models import BankAccount
from .serializers import BankAccountSerializer

logger = structlog.get_logger(__name__)


@log_api_viewset(log_api_call)
class BankAccountViewSet(viewsets.ModelViewSet):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer

    def retrieve(self, request, pk=None):
        account_number = pk
        queryset = self.get_queryset()
        account = get_object_or_404(queryset, account_number=account_number)
        serializer = self.get_serializer(account)
        return Response(serializer.data)

    def update(self, request, pk=None):
        account_number = pk
        queryset = self.get_queryset()
        account = get_object_or_404(queryset, account_number=account_number)
        serializer = self.get_serializer(account, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        account_number = pk
        queryset = self.get_queryset()
        account = get_object_or_404(queryset, account_number=account_number)
        serializer = self.get_serializer(account, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        account_number = pk
        queryset = self.get_queryset()
        account = get_object_or_404(queryset, account_number=account_number)
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
