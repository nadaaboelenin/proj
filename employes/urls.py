from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_employee, name='add_employee'),
    path('', views.list_employees, name='list_employees'),
    path('delete_by_age/', views.delete_by_age, name='delete_by_age'),
    path('update_salary/', views.update_salary, name='update_salary'),
]
