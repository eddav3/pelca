from django.contrib import admin
from provider.models import Provider
# Register your models here.


class ProviderAdmin(admin.ModelAdmin):

    search_fields = ['first_name','nit']
    list_display = ['first_name', 'last_name', 'nit', 'contactphone', 'typeprovider', ]


admin.site.register(Provider,ProviderAdmin)

