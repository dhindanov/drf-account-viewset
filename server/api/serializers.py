from rest_framework import serializers

from api.models import BankAccount


class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = ['account_number', 'account_holder', 'balance', 'created_at', 'updated_at']
