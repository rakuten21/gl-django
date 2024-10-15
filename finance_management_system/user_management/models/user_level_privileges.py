from  django.db import models
from django.utils import timezone
from .user_levels import UserLevels
from .privileges import Privileges

class UserLevelPrivileges(models.Model):
    user_level_privilege_id = models.AutoField(primary_key=True)
    user_level = models.ForeignKey(UserLevels, on_delete=models.CASCADE)
    privilege = models.ForeignKey(Privileges, on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(default=timezone.now)
    datetime_updated = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('user_level', 'privilege')

    def __str__(self):
        return f'{self.user_level} - {self.privilege}'