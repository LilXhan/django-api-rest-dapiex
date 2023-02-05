from django.db import models
from django.utils import timezone

class Task(models.Model):
    name = models.CharField(max_length=100)
    priority = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True)

    def finished(self):
        self.finished_at = timezone.now()
        return self.save()