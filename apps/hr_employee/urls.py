from django.conf.urls import url, include
from . import views

app_name = 'hr_employee'

urlpatterns = [
    url(r'^$', views.index, name='main'),
    # url(r'^employees/$', views.employees, name='employees'),
]