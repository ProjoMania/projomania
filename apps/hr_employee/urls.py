from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

app_name = 'hr_employee'

urlpatterns = [
    # url(r'^$', views.index, name='main'),
    url(r'^employees/form/(?P<pk>[0-9]+)', views.EmployeeDetailView.as_view(), name='employees_form'),
    url(r'^employees/create/', views.EmployeeCreateView.as_view(), name='employees_create'),
    url(r'^employees/', views.EmployeeIndexView.as_view(), name='employees'),
    url(r'^departments/form/(?P<pk>[0-9]+)', views.DepartmentDetailView.as_view(), name='departments_form'),
    url(r'^departments/', views.DepartmentIndexView.as_view(), name='departments'),
    url(r'^', TemplateView.as_view(template_name="hr_employee/index.html"), name='main'),
]
