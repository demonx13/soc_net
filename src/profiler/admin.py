from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserNet
from django.utils.translation import gettext, gettext_lazy as _


# Register your models here.

class SocNetAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'middle_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('info'), {'fields': ('first_login', 'phone', 'gender',        'avatar')}),
    )

    list_display = ('username', 'email', 'first_name', 'last_name', 'phone', 'is_staff')


admin.site.register(UserNet, SocNetAdmin)
