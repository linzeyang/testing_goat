from django.contrib import admin

from lists.models import List, Item


class ListAdmin(admin.ModelAdmin):
    """
    """
    pass


class ItemAdmin(admin.ModelAdmin):
    """
    """
    pass

admin.site.register(List, ListAdmin)
admin.site.register(Item, ItemAdmin)
