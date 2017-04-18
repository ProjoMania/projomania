# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from .models import Employee, Department

from django.shortcuts import render

# Create your views here.


# Employees
class EmployeeIndexView(generic.ListView):
    model = Employee


# Departments
class DepartmentIndexView(generic.ListView):
    model = Department
