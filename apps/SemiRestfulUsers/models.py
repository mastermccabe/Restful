from __future__ import unicode_literals

from django.db import models
import re

# Create your models here.

class Validator(models.Manager):
    def is_valid(self, postData):
        errors = {}
        pattern = re.compile('^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not pattern.match(postData['email']):
            errors['email'] = "invalid email"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = Validator()
