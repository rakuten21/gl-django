from django.db import models
from django.utils import timezone

class UserLevels(models.Model):
    user_level_id = models.AutoField(primary_key=True)
    user_level = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    datetime_created = models.DateTimeField(default=timezone.now)
    datetime_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user_level