from django.http import JsonResponse
from fms.models import ChartOfAccounts

def deactivate_account(request, account_code):
    if request.method == 'POST':
        try:
            account = ChartOfAccounts.objects.get(account_code=account_code)
            account.account_status = False
            account.save()

            return JsonResponse({"success": True})
        except ChartOfAccounts.DoesNotExist:
            return JsonResponse({"sucess": False, "error": 'Account not found.'})

    return JsonResponse({"success": False, "message": "Invalid request method."})