from django.shortcuts import render
from django.http import JsonResponse
from fms.models import ChartOfAccounts
from django.utils import timezone

def add_account(request):
    if request.method == 'POST':
        account_code = request.POST.get('account_code')
        account_description = request.POST.get('account_description')
        account_type = request.POST.get('account_type')
        nature_of_log = request.POST.get('nature_of_log')

        errors = {}
        if not account_code:
            errors['account_code'] = 'Account Code is required.'
        if not account_description:
            errors['account_description'] = 'Account Description is required.'
        if not account_type:
            errors['account_type'] = 'Account Type is required.'
        if not nature_of_log:
            errors['nature_of_log'] = 'Nature of Log is required.'
        
        if errors:
            return JsonResponse({"success": False, "errors": errors})
        
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
            return JsonResponse({"success": False, "errors": str(e)})

    return JsonResponse({"success": False, "message": "Invalid request method"})
