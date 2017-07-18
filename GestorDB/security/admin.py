# -*- coding: utf-8 -*-

# Librerias Django:
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Modelos:
from .models import Profile


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
        'get_bio',
        'get_is_owner',
    )
    list_select_related = ('profile', )

    def get_bio(self, instance):
        return instance.profile.bio

    def get_is_owner(self, instance):
        return instance.profile.is_owner

    get_bio.short_description = 'Bio'
    get_is_owner.short_description = "Is Owner"

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)