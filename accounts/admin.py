# accounts/admin.py

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

User = get_user_model()

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    list_display_links = ('username',)
    # 1. FIELDS ON THE USER EDIT PAGE (Detail View)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('full_name', 'email', 'avatar_path')}),
        ('Preferences', {'fields': ('preferred_categories', 'preferred_difficulty')}),
        
        # RESTORED groups and user_permissions for full admin functionality
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}), 
        
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # 2. FIELDS ON THE ADD USER PAGE
    # NOTE: You may want to add custom fields to this if you want to set preferences 
    # when creating a user in the admin.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password', 'password2'), # Note: password1/password2 are handled by the form
        }),
    )

    # 3. COLUMNS ON THE USER LIST PAGE (Main View)
    list_display = (
        'id', 
        'username', 
        'email', 
        'full_name', 
        'preferred_difficulty', # <--- ADDED
        'is_active', 
        'is_staff'
    )
    
    search_fields = ('username', 'email', 'full_name')
    ordering = ('id',)