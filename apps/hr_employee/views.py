# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse
from django.views import generic
from .models import Employee, Department

from django.shortcuts import render

# Create your views here.


# Employees
class EmployeeIndexView(generic.ListView):
    model = Employee


class EmployeeDetailView(generic.DetailView):
    model = Employee


class EmployeeCreateView(generic.CreateView):
    model = Employee
    fields = ['name', 'work_phone', 'work_mobile']
    template_name_suffix = '_create_form'

    def get_success_url(self):
        return reverse('hr_employee:employees')


# Departments
class DepartmentIndexView(generic.ListView):
    model = Department


class DepartmentDetailView(generic.DetailView):
    model = Department
