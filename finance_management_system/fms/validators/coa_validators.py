# coa_validators.py
from fms.models import ChartOfAccounts

def validate_account_data(account_code, account_description, account_type, nature_of_log, is_live=False):
    account_errors = {}

    # Validate Account Code
    if not account_code:
        account_errors['account_code'] = 'Account Code is required.'
    elif len(account_code) < 3 or len(account_code) > 8:
        account_errors['account_code'] = 'Account Code must be between 3 and 8 digits.'
    elif not account_code.isdigit():
        account_errors['account_code'] = 'Account Code must only contain numbers.'
    else:
        # Check if the account code already exists
        if ChartOfAccounts.objects.filter(account_code=account_code).exists():
            account_errors['account_code'] = 'Account Code already exists.'

    # Validate Account Description
    if not account_description:
        account_errors['account_description'] = 'Account Description is required.'
    elif len(account_description) < 3:
        account_errors['account_description'] = 'Account Description must be at least 3 characters.'
    elif len(account_description) > 50:
        account_errors['account_description'] = 'Account Description must be no more than 50 characters.'
    else:
        # Check if the account description already exists
        if ChartOfAccounts.objects.filter(account_description=account_description).exists():
            account_errors['account_description'] = 'Account Description already exists.'

    # Validate Account Type
    if not account_type:
        account_errors['account_type'] = 'Account Type is required.'

    # Validate Nature of Log
    if not nature_of_log:
        account_errors['nature_of_log'] = 'Nature of Log is required.'

    return account_errors
