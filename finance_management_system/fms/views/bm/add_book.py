from django.shortcuts import render, redirect
from django.contrib import messages
from fms.models.bm.mb_model import Book

def add_book(request):
    if request.method == 'POST':
        book_name = request.POST['book_name']
        book_type = request.POST['book_type']
        try:
            # Create and save the new book
            new_book = Book(book_name=book_name, book_type=book_type)
            new_book.save()
            messages.success(request, 'Book added successfully!')
            return redirect('manage_books')
        except Exception as e:
            messages.error(request, f'Error adding book: {str(e)}')
            return redirect('manage_books')
    else:
        return redirect('manage_books')