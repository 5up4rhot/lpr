from .models import Profile, Structure, Department
# CBVs
from django.views.generic import ListView, DetailView


class StructureListView(ListView):
    model = Structure
    context_object_name = 'structures'
    template_name = 'people_app/structure_list.html'


class StructureDetailView(DetailView):
    model = Structure
    template_name = 'people_app/structure_detail.html'


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'people_app/profile_detail.html'


class DepartmentListView(ListView):
    model = Department
    context_object_name = 'departments'
    template_name = 'people_app/department_list.html'


class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'people_app/department_detail.html'
