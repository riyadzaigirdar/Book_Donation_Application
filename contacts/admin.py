from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'book_id', 'book', 'email', 'phone', 'date')
    list_display_links = ('name', 'book_id', 'book')
    list_filter = ('name', 'book')
    list_per_page = 25


admin.site.register(Contact, ContactAdmin)
