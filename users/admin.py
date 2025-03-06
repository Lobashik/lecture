from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import Book


User = get_user_model()


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'first_name', 'last_name', 'username', ]
    list_display_links = ['email', 'username']
    search_fields = ['first_name', 'last_name', ]
    readonly_fields = ['username', 'id']
    list_filter = ['first_name', 'last_name', ]
    fieldsets = (
        (
            "Основная информация", {
            'fields': ('email', 'first_name', 'last_name')
        }),
        (
            "Админская информация", {
                'fields': ('username', 'id', 'date_of_birth')
            }
        )
    )


class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'author', ]
    radio_fields = {
        'author': admin.HORIZONTAL
    }


admin.site.register(User, UserAdmin)
admin.site.register(Book, BookAdmin)