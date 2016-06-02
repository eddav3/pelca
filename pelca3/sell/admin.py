from django.contrib import admin
from sell.models import Sell
from sell.models import SellDetail
# Register your models here.


class SellDetailAdmin(admin.TabularInline):
    model = SellDetail
    exclude = ['subtotal']


class SaleAdmin(admin.ModelAdmin):
    raw_id_fields = ['customer']
    inlines = [
        SellDetailAdmin,
    ]

    list_display = ['date', 'employee']
    search_fields = ['customer']
    list_filter = ['date', 'employee']

admin.site.register(Sell,SaleAdmin)

