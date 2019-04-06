from django.shortcuts import render
from .models import Principle, Reform, Opinion, QA

from django.views.generic import ListView, DetailView
# Create your views here.


def index(request):
    principles_list = Principle.objects.all()
    return render(request, 'principles_app/index.html', {'principles_list': principles_list})


class PrincipleListView(ListView):
    queryset = Principle.objects.all()
    context_object_name = 'principles'
    template_name = 'principles_app/declaration.html'


def program(request):
    return render(request, 'principles_app/reform_list.html')


def constitutional(request):
    reforms = Reform.objects.filter(header="law")
    title = "Констутиционно-правовые реформы"
    template = 'principles_app/program.html'
    return render(request, template, {'title': title, 'reforms': reforms})


def justice(request):
    reforms = Reform.objects.filter(header="justice")
    title = "Судебно-правоохранительная реформа"
    template = 'principles_app/program.html'
    return render(request, template, {'title': title, 'reforms': reforms})


def social(request):
    reforms = Reform.objects.filter(header="social")
    title = "Социальные рефомы"
    template = 'principles_app/program.html'
    return render(request, template, {'title': title, 'reforms': reforms})


def economic(request):
    reforms = Reform.objects.filter(header="economic")
    title = "Экономические реформы"
    template = 'principles_app/program.html'
    return render(request, template, {'title': title, 'reforms': reforms})


def military(request):
    reforms = Reform.objects.filter(header="military")
    title = "Военно-промышленная реформа"
    template = 'principles_app/program.html'
    return render(request, template, {'title': title, 'reforms': reforms})


def fp(request):
    reforms = Reform.objects.filter(header="fp")
    title = "Внешнеполитическая реформа"
    template = 'principles_app/program.html'
    return render(request, template, {'title': title, 'reforms': reforms})


class OpinionListView(ListView):
    queryset = Opinion.objects.all()
    context_object_name = 'opinions'
    template_name = 'principles_app/opinion_list.html'


def qa(request):
    qa_list_all = QA.objects.order_by('subject')
    template = 'principles_app/qa_list.html'
    return render(request, template, {'qa_list_all': qa_list_all})
