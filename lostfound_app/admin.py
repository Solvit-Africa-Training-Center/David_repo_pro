from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'post_type', 'user', 'location', 'date', 'created_at')
    list_filter = ('post_type', 'date', 'created_at')
    search_fields = ('title', 'description', 'location', 'user__username')
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'
