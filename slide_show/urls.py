from django.urls import path, include
from . import views

urlpatterns = [
    path('create', views.create_slide, name='create_slide'),
    path('clone', views.clone_slide, name='clone_slide'),
    path('', views.index, name='index'),
]