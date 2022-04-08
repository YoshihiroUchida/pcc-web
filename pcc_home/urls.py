from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('programming/', views.programming, name = 'programming'),
    path('news/', views.news, name = 'news'),
    path('news_create/', views.news_create, name = 'news_create'),
    path('setting/', views.setting, name = 'setting'),
    path('programming/edit/<int:num>', views.edit, name = 'edit'),
]
