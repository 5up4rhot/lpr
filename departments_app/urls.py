from django.urls import path
from . import views

app_name = 'departments_app'
urlpatterns = [
    path('', views.DepartmentListView.as_view(), name='department_list'),
    path('<region>/', views.DepartmentListView.as_view(), name='department_detail'),
]
