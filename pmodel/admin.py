from django.contrib import admin
from pmodel.models import Pmodel
# Register your models here.


class PmodelAdmin(admin.ModelAdmin):

    search_fields = ['name']
    list_display = ['name', 'Description']


admin.site.register(Pmodel, PmodelAdmin)
