from django.contrib import admin
from employee.models import Employee
from employee.models import EmployeePosition
from employee.models import PositionDetail


class PositionDetailAdmin(admin.TabularInline):
    model = PositionDetail


class EmployeeAdmin(admin.ModelAdmin):

    list_filter = ['gender', 'position']
    list_display = ['first_name', 'position', 'birthday', 'nit', 'salario']
    search_fields = ['first_name', 'nit', 'position']


class EmployeePositionAdmin(admin.ModelAdmin):
    inlines = [
        PositionDetailAdmin,
    ]
    list_display = ['first_name', 'salary', 'start', 'end']


# Register your models here.
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(EmployeePosition, EmployeePositionAdmin)