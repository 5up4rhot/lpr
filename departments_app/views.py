from .models import Department
# CBVs
from django.views.generic import ListView, DetailView


class DepartmentListView(ListView):
    model = Department
    context_object_name = 'departments'
    template_name = 'departments_app/department_list.html'


class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'departments_app/department_detail.html'
