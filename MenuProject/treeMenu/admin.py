from django.contrib import admin
from .models import Menu, Item


class ItemInLine(admin.TabularInline):
    model = Item


class MenuAdmin(admin.ModelAdmin):
    inlines = [
        ItemInLine,
    ]


admin.site.register(Menu, MenuAdmin)
admin.site.register(Item)
