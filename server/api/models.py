from django.conf import settings
from django.db import models
from pydantic import BaseModel, Field


class BankAccount(models.Model):
    account_number = models.CharField(max_length=255, unique=True)
    account_holder = models.TextField()
    balance = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
