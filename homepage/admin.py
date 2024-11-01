from django.contrib import admin

# Register your models here.
from .models import New, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','id')

class NewAdmin(admin.ModelAdmin):
    list_display = ('title', 'text','author', 'date', 'id')

admin.site.register(Category, CategoryAdmin)
admin.site.register(New, NewAdmin)