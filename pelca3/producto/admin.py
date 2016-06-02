from django.contrib import admin
from producto.models import Producto

# Register your models here.


class ProductoAdmin(admin.ModelAdmin):
    list_display = ['ProductName','Brand','Price','existence','min_existence']
    search_fields = ['ProductName']
    list_filter = ['Brand']


admin.site.register(Producto,ProductoAdmin)