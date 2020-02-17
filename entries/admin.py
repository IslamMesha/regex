from django.contrib import admin

from entries.models import Entry


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_filter = ('user',)
    search_fields = ('test_string',)
    list_display = ('pattern', 'test_string', 'user',)
    fieldsets = (
        ('Regular Expression', {'fields': ['pattern', 'test_string']}),
        ('Other Information', {'fields': ['user', 'date_added']}),
    )
