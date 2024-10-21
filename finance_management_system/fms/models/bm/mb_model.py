from django.db import models
from django.utils import timezone

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=255)
    book_type = models.IntegerField()
    book_status = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.book_name
    
    class Meta:
        db_table = 'book'
