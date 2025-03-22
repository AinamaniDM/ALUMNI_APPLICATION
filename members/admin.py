# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile

# Define an inline admin descriptor for Profile model
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

# Extend the UserAdmin to include the Profile inline
class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

    # Optional: Customize the fields displayed in the User list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

# Unregister the default User admin and register the custom one
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Optionally, register the Profile model separately if you want to manage profiles directly
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'graduation_year', 'current_employer')
    search_fields = ('user__username', 'full_name')