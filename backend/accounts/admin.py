from django.contrib import admin

# Register your models here.
# from .models import UserAccount

from .models import User

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'is_active',
                     'is_staff', 'is_superuser')

admin.site.register(User, CustomUserAdmin)
