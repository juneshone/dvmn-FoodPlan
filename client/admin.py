from django.contrib import admin

from client.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ('last_name', 'first_name', 'username',)
    list_display = ('last_name', 'first_name', 'username',)
