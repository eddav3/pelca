from django.contrib import admin
from brand.models import Brand
# Register your models here.


class BrandAdmin(admin.ModelAdmin):

    search_fields = ['name']
    list_display = ['name', 'Description']


admin.site.register(Brand, BrandAdmin)
