# get_account.py
from django.http import JsonResponse
from fms.models import ChartOfAccounts

def get_account(request, account_id):
    try:
        account = ChartOfAccounts.objects.get(id=account_id)
        return JsonResponse({
            'account_code': account.account_code,
            'account_description': account.account_description,
            'account_type': account.account_type,
            'nature_of_log': account.nature_of_log,
        })
    except ChartOfAccounts.DoesNotExist:
        return JsonResponse({"error": "Account not found"}, status=404)
