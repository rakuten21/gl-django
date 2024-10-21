from django.db import models
from django.utils import timezone

class AccountType(models.TextChoices):
    ASSET = 'Asset', 'Asset'
    LIABILITY = 'Liability', 'Liability'
    EQUITY = 'Equity', 'Equity'
    REVENUE = 'Revenue', 'Revenue'
    EXPENSE = 'Expense', 'Expense'

class NatureOfLog(models.TextChoices):
    DEBIT = 'Debit', 'Debit'
    CREDIT = 'Credit', 'Credit'

class ChartOfAccounts(models.Model):
    account_code = models.PositiveIntegerField(unique=True)
    account_description = models.CharField(max_length=255, unique=True)
    account_type = models.CharField(
        max_length=20,
        choices=AccountType.choices
    )
    nature_of_log = models.CharField(
        max_length=6,
        choices=NatureOfLog.choices
    )
    account_status = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.account_code} - {self.account_description}"

    class Meta:
        db_table = 'chart_of_accounts'

