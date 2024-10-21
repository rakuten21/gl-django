from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from fms.models.bm.bt_model import BookType

def manage_books(request):
    book_types = BookType.objects.all()  # Retrieve all book types
    context = {
        'book_types': book_types
    }
    return render(request, 'bm/bm_manage_types.html', context)

# Validation function (can be reused)
def validate_book_type_data(book_type_name, description, book_type_id=None):
    book_type_errors = {}

    # Validate Book Type Name
    if not book_type_name:
        book_type_errors['book_type_name'] = 'Book type name is required.'
    elif len(book_type_name) < 3:
        book_type_errors['book_type_name'] = 'Book type name must be at least 3 characters.'
    elif len(book_type_name) > 50:
        book_type_errors['book_type_name'] = 'Book type name must be no more than 50 characters.'
    else:
        # Check if the book type name already exists (excluding current book type)
        existing_book_type = BookType.objects.filter(book_type_name=book_type_name).exclude(id=book_type_id)
        if existing_book_type.exists():
            book_type_errors['book_type_name'] = 'Book type name already exists.'

    # Validate Description
    if not description:
        book_type_errors['description'] = 'Description is required.'
    elif len(description) < 3:
        book_type_errors['description'] = 'Description must be at least 3 characters.'

    return book_type_errors

# Edit Book Type View
def edit_book_type(request, book_type_id):
    book_type = get_object_or_404(BookType, id=book_type_id)

    if request.method == 'POST':
        # Get updated data from the form
        book_type_name = request.POST.get('edit_book_type_name')
        description = request.POST.get('edit_book_type_description')

        # Validate the updated data
        errors = validate_book_type_data(book_type_name, description)

        if errors:
            for field, error_message in errors.items():
                messages.error(request, error_message)
            return redirect('manage_books')

        # Update the book type fields
        book_type.book_type_name = book_type_name
        book_type.description = description
        book_type.save()

        messages.success(request, 'Book type updated successfully!')
        return redirect('manage_books')

    return render(request, 'bm/bm_manage_types.html')