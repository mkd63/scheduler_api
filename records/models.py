from django.db import models
from users.models import Users
# Create your models here.
class Records(models.Model):

    event_dateTime = models.DateTimeField(null=False)
    event_agenda = models.CharField(null=False, max_length=150)
    user = models.ForeignKey(Users, on_delete = models.CASCADE)

    def __str__(self):
        return self.name
