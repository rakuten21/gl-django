from django.shortcuts import render
from ..models.bm.bt_model import BookType
from ..models.coa_model import ChartOfAccounts

def chart_of_accounts(request):
    accounts = ChartOfAccounts.objects.all().order_by('account_code')
    return render(request, 'coa/coa_tab_panel.html', {'accounts': accounts})

def manage_books(request):
    book_types = BookType.objects.all()
    return render(request, 'bm/bm_tab_panel.html', {'book_types': book_types})