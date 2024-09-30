from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'nombre', 'is_staff', 'is_active')
    search_fields = ('email', 'nombre')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'nombre', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nombre', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

admin.site.register(Usuario, CustomUserAdmin)
