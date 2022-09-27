from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  # '': 홈페이지
    path('create/', views.create),
]
