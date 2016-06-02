from django.contrib import admin
from customer.models import Customer
from customer.models import Customertype


class CustomerAdmin(admin.ModelAdmin):

    search_fields = ['first_name','nit']
    list_display = ['first_name', 'last_name', 'nit','customertype','discount' ]


admin.site.register(Customer,CustomerAdmin)
admin.site.register(Customertype)
