from django.contrib import admin
from . models import Item

# Register your models here.
class TableAdmin(admin.ModelAdmin):
    list_name = ('name', 'cost', 'description')

admin.site.register(Item, TableAdmin)