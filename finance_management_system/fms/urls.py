from django.urls import path
from .views import views
from .views.coa import add_account, edit_account, deactivate_account, get_account
from .views.bm_bt import add_book_type, edit_book_type
from .views.bm import add_book

urlpatterns = [
    path('chart_of_accounts/', views.chart_of_accounts, name='chart_of_accounts'),
    path('add_account/', add_account.add_account, name='add_account'),
    path('edit_account/<int:account_id>/', edit_account.edit_account, name='edit_account'),
    path('get_account/<int:account_id>/', get_account.get_account, name='get_account'),
    
    # Book Management URLs
    path('books_management/manage_books/', views.manage_books, name='manage_books'),
    path('books_management/add_book/', add_book.add_book, name='add_book'),  # Add this URL

    path('books_management/add_book_type/', add_book_type.add_book_type, name='add_book_type_page'),
    path('book-type/edit/<int:book_type_id>/', edit_book_type.edit_book_type, name='edit_book_type'),
]
