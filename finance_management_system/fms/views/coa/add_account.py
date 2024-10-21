# add_account.py
from django.shortcuts import render
from django.http import JsonResponse
from fms.models import ChartOfAccounts
from django.utils import timezone
from fms.validators.coa_validators import validate_account_data

def add_account(request):
    if request.method == 'POST':
        account_code = request.POST.get('account_code')
        account_description = request.POST.get('account_description')
        account_type = request.POST.get('account_type')
        nature_of_log = request.POST.get('nature_of_log')

        # Live validation
        if request.POST.get('live_validation'):
            account_errors = validate_account_data(account_code, account_description, account_type, nature_of_log, is_live=True)
            return JsonResponse({'success': not bool(account_errors), 'errors': account_errors})

        account_errors = validate_account_data(account_code, account_description, account_type, nature_of_log)
        
        if account_errors:
            return JsonResponse({"success": False, "errors": account_errors})
        
        try:
            ChartOfAccounts.objects.create(
                account_code=account_code,
                account_description=account_description,
                account_type=account_type,
                nature_of_log=nature_of_log,
                account_status=True,
                created_at=timezone.now(),
                updated_at=timezone.now()
            )

            return JsonResponse({"success": True})
        
        except Exception as e:
            return JsonResponse({"success": False, "errors": "An error occurred. Please try again later."})

    return JsonResponse({"success": False, "message": "Invalid request method"})
