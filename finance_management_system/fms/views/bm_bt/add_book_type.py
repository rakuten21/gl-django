from django.shortcuts import render, redirect
from django.contrib import messages
from fms.models.bm.bt_model import BookType

def validate_book_type_data(book_type_name, description):
    book_type_errors = {}

    # Validate Book Type Name
    if not book_type_name:
        book_type_errors['book_type_name'] = 'Book type name is required.'
    elif len(book_type_name) < 3:
        book_type_errors['book_type_name'] = 'Book type name must be at least 3 characters.'
    elif len(book_type_name) > 50:
        book_type_errors['book_type_name'] = 'Book type name must be no more than 50 characters.'
    else:
        # Check if the book type name already exists
        if BookType.objects.filter(book_type_name=book_type_name).exists():
            book_type_errors['book_type_name'] = 'Book type name already exists.'

    # Validate Description
    if not description:
        book_type_errors['description'] = 'Description is required.'
    elif len(description) < 3:
        book_type_errors['description'] = 'Description must be at least 3 characters.'

    return book_type_errors

def add_book_type(request):
    if request.method == 'POST':
        # Get the form data
        book_type_name = request.POST.get('book_type_name')
        description = request.POST.get('book_type_description')

        # Validate the form data
        errors = validate_book_type_data(book_type_name, description)

        # If there are errors, display them
        if errors:
            for field, error_message in errors.items():
                messages.error(request, error_message)
            return redirect('manage_books')  # Redirect back to the form

        # If no errors, save the book type
        BookType.objects.create(book_type_name=book_type_name, description=description)
        messages.success(request, 'Book type added successfully!')
        return redirect('manage_books')  # Corrected the redirect URL

    # If GET request, render the form page
    return render(request, 'bm/bm_manage_types.html')
