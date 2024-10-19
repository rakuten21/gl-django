from django.urls import path
from .views import views
from .views.coa import add_account, edit_account, deactivate_account

urlpatterns = [
    # display the chart of accounts
    path('chart_of_accounts/', views.chart_of_accounts, name='chart_of_accounts'),
    
    # for adding account
    path('add_account/', add_account.add_account, name='add_account'),

    # for editing account
    # for deactivating accoung
    path('deactivate_account/<int:account_code>/', deactivate_account.deactivate_account, name='deactivate_account'),
    # path('edit_account/<int:account_id>/', edit_account.edit_account, name='edit_account'),
    path('books_management/manage_books/', views.manage_books, name='manage_books'),
]
