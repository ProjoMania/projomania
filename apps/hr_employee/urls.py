from django.conf.urls import url, include
from django.views.generic import TemplateView

from . import views

app_name = 'hr_employee'

urlpatterns = [
    # url(r'^$', views.index, name='main'),
    url(r'^$', TemplateView.as_view(template_name="hr_employee/index.html"), name='main'),
    url(r'^employees/', views.EmployeeIndexView.as_view(), name='employees'),
    url(r'^departments/', views.DepartmentIndexView.as_view(), name='departments'),
]