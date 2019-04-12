from django.urls import path
from . import views

app_name = 'people_app'
urlpatterns = [
    path('', views.StructureListView.as_view(), name='structure_list'),
    path('structure/<slug:slug>/', views.StructureDetailView.as_view(), name='structure_detail'),
    path('<slug:slug>/', views.ProfileDetailView.as_view(), name='profile_detail'),
    path('departments/', views.DepartmentListView.as_view(), name='department_list'),
    path('department/<region>/', views.DepartmentListView.as_view(), name='department_detail'),
]
