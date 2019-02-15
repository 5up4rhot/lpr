from django.urls import path
from . import views

app_name = 'principles_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('declaration/', views.PrincipleListView.as_view(), name='declaration'),
    path('program/', views.program, name='program'),
    path('program/constitutional/', views.constitutional, name='constitutional'),
    path('program/justice/', views.justice, name='justice'),
    path('program/social/', views.social, name='social'),
    path('program/economic/', views.economic, name='economic'),
    path('program/military/', views.military, name='military'),
    path('program/foreign-policy/', views.fp, name='fp'),
    path('platform/', views.OpinionListView.as_view(), name='platform'),
    path('questions/', views.qa, name='questions'),
]
