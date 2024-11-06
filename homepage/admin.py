from django.contrib import admin

# Register your models here.
from .models import New, Category, Region


# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name','id')
#
# class NewAdmin(admin.ModelAdmin):
#     list_display = ('title', 'text','author', 'date', 'id')

admin.site.register(Category)
# admin.site.register(CategoryAdmin)
admin.site.register(New)
admin.site.register(Region)
# admin.site.register(NewAdmin)
