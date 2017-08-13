# -*- coding: utf-8 -*-

# Python's Libraries
from __future__ import unicode_literals

# Django's Libraries
from django.db import models


class EstafetaAmbiente(models.Model):
    clave = models.CharField(max_length=144, unique=True)
    url = models.CharField(max_length=300, null=True, blank=True)
    login = models.CharField(max_length=144, null=True, blank=True)
    password = models.CharField(max_length=144, null=True, blank=True)
    quadrant = models.IntegerField(default=1)
    suscriber_id = models.CharField(max_length=144, null=True, blank=True)
    paper_type = models.IntegerField(default=1)
    customer_number = models.CharField(max_length=144, null=True, blank=True)

    cot_url = models.CharField(max_length=300, null=True, blank=True)
    cot_id_usuario = models.CharField(max_length=144, null=True, blank=True)
    cot_usuario = models.CharField(max_length=144, null=True, blank=True)
    cot_contra = models.CharField(max_length=144, null=True, blank=True)

    is_active = models.BooleanField(default=True)

    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.clave
