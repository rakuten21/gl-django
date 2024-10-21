from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from fms.models import ChartOfAccounts
from django.utils import timezone
from fms.validators.coa_validators import validate_account_data

def edit_account(request, account_id):
    account = get_object_or_404(ChartOfAccounts, id=account_id)

    if request.method == 'POST':
        account_code = request.POST.get('account_code')
        account_description = request.POST.get('account_description')
        account_type = request.POST.get('account_type')
        nature_of_log = request.POST.get('nature_of_log')

        if request.POST.get('live_validation'):
            errors = validate_account_data(account_code, account_description, account_type, nature_of_log)
            
            return JsonResponse(errors)

        errors = validate_account_data(account_code, account_description, account_type, nature_of_log)

        if errors:
            return JsonResponse({"success": False, "errors": errors})
        
        try:
            account.account_code = account_code
            account.account_description = account_description
            account.account_type = account_type
            account.nature_of_log = nature_of_log
            account.updated_at = timezone.now()
            account.save()

            return JsonResponse({"success": True})
        
        except Exception as e:
            return JsonResponse({"success": False, "errors": "An error occured. Please try again later."})
        
    return JsonResponse({"success": False, "message": "Invalid request method"})