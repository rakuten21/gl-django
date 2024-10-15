from django.db import models
from django.utils import timezone
from .user_levels import UserLevels
from .account_status import AccountStatus

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    user_title = models.CharField(max_length=100)
    user_level = models.ForeignKey(UserLevels, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=10, 
        choices=AccountStatus.choices, 
        default=AccountStatus.ACTIVE
    )
    datetime_created = models.DateTimeField(default=timezone.now)
    datetime_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username