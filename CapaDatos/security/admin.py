# -*- coding: utf-8 -*-

# Librerias Django:
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Modelos:
from .models import Profile
from .models import Log


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profiles'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_staff',
        'get_estafeta',
    )
    list_select_related = ('profile', )

    def get_estafeta(self, instance):
        return instance.profile.estafeta

    get_estafeta.short_description = 'Estafeta'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


@admin.register(Log)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'guia',
        'comentarios',
        'status',
        'created_by',
        'created_date',
    )
