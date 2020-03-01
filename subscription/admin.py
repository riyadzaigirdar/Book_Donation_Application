from django.contrib import admin
from .models import Subscribe


class SubcribeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    list_display_links = ('name',)
    list_filter = ('name',)
    search_fields = ('name', 'email')
    list_per_page = 25


admin.site.register(Subscribe, SubcribeAdmin)
