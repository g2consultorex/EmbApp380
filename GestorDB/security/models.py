# -*- coding: utf-8 -*-

# Libreria Django:
from __future__ import unicode_literals
from django.db import models

# Libreria Django Signals:
from django.db.models.signals import post_save
from django.dispatch import receiver

# Otros modelos:
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    comentarios = models.TextField(blank=True)
    is_owner = models.BooleanField(default=False)

    def __str_(self):
        nombre_completo = self.user.get_full_name()
        return nombre_completo

    def __unicode__(self):
        nombre_completo = self.user.get_full_name()
        return nombre_completo


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
