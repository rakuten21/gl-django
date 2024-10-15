from django.db import models

class ChartOfAccounts(models.Model):
    account_id = models.AutoField(primary_key=True)  # Explicitly define the primary key
    account_code = models.IntegerField(unique=True)
    account_description = models.CharField(max_length=100, unique=True)
    account_type = models.CharField(max_length=10)
    account_status = models.CharField(max_length=10, choices=[('Active', 'Active'), ('Archived', 'Archived')], default='Active')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'chart_of_accounts'  # Specify the correct table name
