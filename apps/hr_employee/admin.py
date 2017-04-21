# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Employee, Department
# Register your models here.


## Employees
class EmployeeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Employee, EmployeeAdmin)


## Departments
class EmployeeInline(admin.TabularInline):
    model = Employee
    extra = 3


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'manager']
    fieldsets = [
        (None, {'fields': ['name', 'manager']}),
        ]

admin.site.register(Department, DepartmentAdmin)
