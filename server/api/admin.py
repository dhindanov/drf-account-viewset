from django.contrib import admin
from api.models import BankAccount

@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('account_number', 'account_holder', 'balance', 'created_at', 'updated_at')
    search_fields = ('account_number', 'account_holder')
    ordering = ('-created_at',)
