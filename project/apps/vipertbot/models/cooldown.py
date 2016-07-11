from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Cooldown(models.Model):
    user = models.ForeignKey('auth.User')
    name = models.CharField(max_length=100)
    start_time = models.DateTimeField()

    class Meta:
        app_label = 'vipertbot'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
