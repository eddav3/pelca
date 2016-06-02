from django.contrib import admin
from category.models import Category

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):

    search_fields = ['categoryname']
    list_display = ['categoryname', 'description']


admin.site.register(Category, CategoryAdmin)
