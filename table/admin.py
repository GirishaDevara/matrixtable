from django.contrib import admin
from . models import Item, employee

# Register your models here.
# class TableAdmin(admin.ModelAdmin):
#     list_name = ('name', 'cost', 'description')

admin.site.register(Item)
admin.site.register(employee)
