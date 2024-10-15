from django.shortcuts import render, redirect
from django.contrib import messages
from fms.models import ChartOfAccounts
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def add_account(request):
    if request.method == 'POST':
        account_code = request.POST.get('account_code')
        account_description = request.POST.get('account_description')
        account_type = request.POST.get('account_type')
        account_status = request.POST.get('account_status', 'Active')

        # check if the account already exists
        if ChartOfAccounts.objects.filter(account_code=account_code).exists():
            messages.error(request, 'Account code already exists')
            return redirect('chart_of_accounts')
        
        # check if the account description already exists
        if ChartOfAccounts.objects.filter(account_description=account_description).exists():
            messages.error(request, 'Account description already exists')
            return redirect('chart_of_accounts')
        
        # check if both the account code and description already exist
        if ChartOfAccounts.objects.filter(account_code=account_code, account_description=account_description).exists():
            messages.error(request, 'Account code and description already exist')
            return redirect('chart_of_accounts')
                
        new_account = ChartOfAccounts(
            account_code=account_code, 
            account_description=account_description, 
            account_type=account_type,
            account_status=account_status
        )

        # saving the user's input
        new_account.save()

        # display success message
        messages.success(request, 'Account added successfully!')
        return redirect('chart_of_accounts')

    # pass them to the template
    return render(request, 'chart_of_accounts/coa.html')
