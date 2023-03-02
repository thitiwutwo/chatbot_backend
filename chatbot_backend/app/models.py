from django.db import models
from django.utils import timezone

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    password = models.CharField(max_length=1000, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Users"