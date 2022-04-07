from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('program/', views.program, name = 'program'),
    path('news/', views.news, name = 'news'),
    path('setting/', views.setting, name = 'setting'),
    path('program/edit/<int:num>', views.edit, name = 'edit'),
]
