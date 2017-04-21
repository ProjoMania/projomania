# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(verbose_name='Employee Name', null=False, blank=False, max_length=64, )
    personal_phone = models.CharField(verbose_name='Personal Phone', max_length=28, )
    personal_mobile = models.CharField(verbose_name='Personal Mobile', max_length=28, )
    personal_email = models.EmailField(verbose_name='Personal Email', )
    work_phone = models.CharField(verbose_name='Work Phone', max_length=28, )
    work_mobile = models.CharField(verbose_name='Work Mobile', max_length=28, )
    work_email = models.EmailField(verbose_name='Work Email', )

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(verbose_name='Department Name', null=False, blank=False, max_length=64, )
    manager = models.ForeignKey(Employee, )

    def __str__(self):
        return self.name

# The model Employee uses Department, but the definition of the Department is after the Employee.
# The following line is a work-around solution to add the field (relation) after declaring the Department.
Employee.department = models.ForeignKey(Department, )
