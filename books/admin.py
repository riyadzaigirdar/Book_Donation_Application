from django.contrib import admin

from .models import Book

from .models import Category


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_publised',
                    'author', 'list_date', 'category')
    list_display_links = ('id', 'name')
    list_filter = ('category',)
    list_editable = ('is_publised',)
    search_fields = ('name', 'author', 'address')
    list_per_page = 25


class CategoryAdmin(admin.ModelAdmin):

    list_per_page = 25
    list_display = ('id', 'category')


admin.site.register(Book, BookAdmin)

admin.site.register(Category, CategoryAdmin)
