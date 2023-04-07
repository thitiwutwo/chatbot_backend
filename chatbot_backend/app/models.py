from django.db import models
from django.utils import timezone

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=100, blank=False)
    # email = models.EmailField(max_length=100, blank=False)
    email = models.CharField(max_length=100, blank=False)
    password = models.CharField(max_length=1000, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Users"

class Files(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='static/')
    intent = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Files"

class Chats(models.Model):
    text = models.CharField(max_length=255, null=True, blank=True)
    sender_id = models.IntegerField()
    is_user = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now_add=True)
    file_url = models.CharField(max_length=255, null=True, blank=True)
    channel = models.ForeignKey('Channels', on_delete=models.CASCADE)
    def __str__(self):
        return self.text or self.file_url
    class Meta:
        verbose_name_plural = "Chats"

class Channels(models.Model):
    name = models.CharField(max_length=255, null=True)
    sender_id = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True) 
    modified = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Channels"