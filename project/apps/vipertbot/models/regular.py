from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Regular(models.Model):
    user = models.ForeignKey('auth.User')
    name = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        app_label = 'vipertbot'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name