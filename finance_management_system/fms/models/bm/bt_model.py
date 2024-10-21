from django.db import models
from django.utils import timezone

class BookType(models.Model):
    book_type_id = models.AutoField(primary_key=True)
    book_type_name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.book_type_name

    class Meta:
        db_table = 'book_type'