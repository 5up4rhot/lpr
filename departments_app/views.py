from .models import Department
# CBVs
from django.views.generic import ListView, DetailView


class DepartmentListView(ListView):
    model = Department
    context_object_name = 'departments'
    template_name = 'departments_app/department_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get("region", "")
        if query:
            matching_query = self.get_queryset().filter(region__alternate_names__icontains=query)
            context['results'] = matching_query
        return context


class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'departments_app/department_detail.html'
