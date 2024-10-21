# from fms.models.bm.bt_model import BookType

# def validate_book_type_data(book_type_name, description):
#     book_type_errors = {}

#     # Validate Book Type Name
#     if not book_type_name:
#         book_type_errors['book_type_name'] = 'Book type name is required.'
#     elif len(book_type_name) < 3:
#         book_type_errors['book_type_name'] = 'Book type name must be at least 3 characters.'
#     elif len(book_type_name) > 50:
#         book_type_errors['book_type_name'] = 'Book type name must be no more than 50 characters.'
#     else:
#         # Check if the book type name already exists
#         if BookType.objects.filter(book_type_name=book_type_name).exists():
#             book_type_errors['book_type_name'] = 'Book type name already exists.'

#     # Validate Description
#     if not description:
#         book_type_errors['description'] = 'Description is required.'
#     elif len(description) < 3:
#         book_type_errors['description'] = 'Description must be at least 3 characters.'

#     return book_type_errors