from django.shortcuts import render
from .models import Principle, Reform, Opinion, QA

from django.views.generic import ListView, DetailView
# Create your views here.


def index(request):
    principles_list_collapsed = Principle.objects.order_by('pk')[:5]
    principles_list_full = Principle.objects.order_by('pk')[5:]
    return render(request, 'principles_app/index.html', {'principles_list_full': principles_list_full,
                                                        'principles_list_collapsed': principles_list_collapsed})

class PrincipleListView(ListView):
    queryset = Principle.objects.all()
    context_object_name = 'principles'
    template_name = 'principles_app/principle_list.html'


def program(request):
    return render(request, 'principles_app/reform_list.html')


def constitutional(request):
    reforms = Reform.objects.filter(header="law")
    title = "Констутиционно-правовые реформы"
    template = 'principles_app/program.html'
    return render(request, template, {'title':title, 'reforms':reforms})


def justice(request):
    reforms = Reform.objects.filter(header="justice")
    title = "Судебно-правоохранительная реформа"
    template = 'principles_app/program.html'
    return render(request, template, {'title':title, 'reforms':reforms})

def social(request):
    reforms = Reform.objects.filter(header="social")
    title = "Социальные рефомы"
    template = 'principles_app/program.html'
    return render(request, template, {'title':title, 'reforms':reforms})

def economic(request):
    reforms = Reform.objects.filter(header="economic")
    title = "Экономические реформы"
    template = 'principles_app/program.html'
    return render(request, template, {'title':title, 'reforms':reforms})

def military(request):
    reforms = Reform.objects.filter(header="military")
    title = "Военно-промышленная реформа"
    template = 'principles_app/program.html'
    return render(request, template, {'title':title, 'reforms':reforms})

def fp(request):
    reforms = Reform.objects.filter(header="fp")
    title = "Внешнеполитическая реформа"
    template = 'principles_app/program.html'
    return render(request, template, {'title':title, 'reforms':reforms})

class OpinionListView(ListView):
    queryset = Opinion.objects.all()
    context_object_name = 'opinions'
    template_name = 'principles_app/opinion_list.html'

def qa(request):
    lib = QA.objects.filter(subject="lib")
    lib_title = 'Либертарианство'
    soc = QA.objects.filter(subject="soc")
    soc_title = 'Социальная поддержка'
    weapon = QA.objects.filter(subject="weapon")
    weapon_title = 'Оружие'
    copyright = QA.objects.filter(subject="copyright")
    copyright_title = 'Копирайт'
    terms = QA.objects.filter(subject="terms")
    terms_title = 'Терминология'
    template = 'principles_app/qa_list.html'
    return render(request, template, {'lib':lib, 'lib_title':lib_title,
                                      'soc':soc, 'soc_title':soc_title,
                                      'weapon':weapon, 'weapon_title':weapon_title,
                                      'copyright':copyright, 'copyright_title':copyright_title,
                                      'terms':terms, 'terms_title':terms_title })
