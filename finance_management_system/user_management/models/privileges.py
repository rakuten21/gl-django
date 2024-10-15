from django.db import models
from django.utils import timezone

class Privileges(models.Model):
    privilege_id = models.AutoField(primary_key=True)
    privilege_name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    datetime_created = models.DateTimeField(default=timezone.now)
    datetime_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.privilege_name