from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Job(models.Model):
    user = models.ForeignKey('auth.User')
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name