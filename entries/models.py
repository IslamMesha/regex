from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pattern = models.CharField(max_length=255)
    test_string = models.CharField(max_length=255)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.pattern

    class Meta:
        verbose_name = 'Entry'
        verbose_name_plural = 'Entries'
