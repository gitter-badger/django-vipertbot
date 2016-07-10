from __future__ import unicode_literals
from django.db import models
from twitch_roles.models import Role

# Create your models here.
# todo: add roles app, create relationship with roles

class Command(models.Model):
    user = models.ForeignKey('auth.User')
    name = models.CharField(max_length=25)
    text = models.TextField(max_length=250)
    cooldown_min = models.IntegerField(default=0)
    roles = models.ManyToManyField(Role)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name