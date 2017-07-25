# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Log


@admin.register(Log)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'titulo',
        'comentarios',
        'status',
        'created_by',
        'created_date',
        'updated_by',
        'updated_date',
    )
