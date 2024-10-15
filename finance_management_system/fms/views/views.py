# views/views.py
from django.shortcuts import render
from ..models.coa_model import ChartOfAccounts

def chart_of_accounts(request):
    accounts = ChartOfAccounts.objects.all().order_by('account_code')
    return render(request, 'coa/coa_table.html', {'accounts': accounts})

def manage_books(request):
    return render(request, 'bm/bm_tab_panel.html')