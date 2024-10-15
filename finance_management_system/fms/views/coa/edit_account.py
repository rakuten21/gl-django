from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from fms.models import ChartOfAccounts

@csrf_exempt  # Use if you're working with AJAX
def edit_account(request, account_id):
    # Get the account object based on the provided ID
    account = get_object_or_404(ChartOfAccounts, account_id=account_id)
    
    if request.method == 'POST':
        # Parse the data manually (replace form handling)
        account_code = request.POST.get('account_code')
        account_description = request.POST.get('account_description')
        account_type = request.POST.get('account_type')
        account_status = request.POST.get('account_status')

        # Ensure that data is not empty and unique
        errors = {}

        if not account_code:
            errors['account_code'] = "Account code is required."
        elif ChartOfAccounts.objects.filter(account_code=account_code).exclude(account_id=account_id).exists():
            errors['account_code'] = "Account code already exists."

        if not account_description:
            errors['account_description'] = "Account description is required."
        elif ChartOfAccounts.objects.filter(account_description=account_description).exclude(account_id=account_id).exists():
            errors['account_description'] = "Account description already exists."

        if not account_type:
            errors['account_type'] = "Account type is required."

        # Return errors as JSON if there are any
        if errors:
            return JsonResponse({'success': False, 'errors': errors})

        # Update the account if no errors
        account.account_code = account_code
        account.account_description = account_description
        account.account_type = account_type
        account.account_status = account_status
        account.save()

        # Return success response
        return JsonResponse({'success': True, 'message': 'Account updated successfully.'})

    return JsonResponse({'success': False, 'message': 'Invalid request method.'})
