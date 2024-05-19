from django.contrib import admin

from account.models import CustomUser

# admin.site.register(CustomUser)

from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('profile_picture',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
