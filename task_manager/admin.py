from django.contrib import admin

from task_manager.users.models import User

# Register your models here


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ['username', 'first_name', 'last_name']
    list_display = [
        'username', 'first_name',
        'last_name', 'date_joined', 'is_superuser'
    ]