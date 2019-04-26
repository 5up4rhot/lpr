from django.urls import path
from . import views

app_name = 'departments_app'
urlpatterns = [
    path('', views.DepartmentListView.as_view(), name='department_list'),
    path('<slug:slug>/', views.DepartmentDetailView.as_view(), name='department_detail'),
]
