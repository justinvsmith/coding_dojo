from django.db import models
from django.contrib import messages
from datetime import datetime, timedelta

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "TV Show title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors['network'] = "TV network should be at least 3 characters"
        if len(postData['description']) < 10:
            errors['description'] = "TV show description should be at least 10 characters"
        if postData['release_date'] > str((datetime.now()-timedelta(days=1))):
            errors['release'] = "Release date must be in the past"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255, blank=False)
    network = models.CharField(max_length=255, blank=False)
    release_date = models.DateField(blank=True)
    description = models.CharField(max_length=255, blank=False)
    objects = ShowManager()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

