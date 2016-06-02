from django.contrib import admin
from buy.models import Buy
from buy.models import BuyDetail

# Register your models here.


class BuyDetailAdmin(admin.TabularInline):
    model = BuyDetail
    exclude = ['subtotal']


class BuyAdmin(admin.ModelAdmin):
    raw_id_fields = ['provider']
    inlines = [
        BuyDetailAdmin,
    ]
    exclude = ['total']
    list_display = ['provider', 'date', 'total']
admin.site.register(Buy, BuyAdmin)
