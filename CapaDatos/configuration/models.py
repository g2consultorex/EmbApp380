# -*- coding: utf-8 -*-

# Python's Libraries
from __future__ import unicode_literals

# Django's Libraries
from django.db import models
from security.models import Profile


class Log(models.Model):

    STATUS = (
        ('ERR', 'ERROR'),
        ('SUC', 'Exito'),
    )

    titulo = models.CharField(max_length=144)
    comentarios = models.TextField()

    status = models.CharField(max_length=3, choices=STATUS, default="REC")
    created_by = models.ForeignKey(
        Profile, related_name='post_creador', null=True)
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_by = models.ForeignKey(
        Profile, related_name='post_actualizador', null=True)
    updated_date = models.DateTimeField(auto_now=True, auto_now_add=False)


class EstafetaUser(models.Model):

    clave = models.CharField(max_length=144, unique=True)
    login = models.CharField(max_length=144)
    password = models.CharField(max_length=144)
    quadrant = models.IntegerField()
    suscriber_id = models.CharField(max_length=144)
    paper_type = models.IntegerField()
    es_principal = models.BooleanField(default=False)

    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.clave
