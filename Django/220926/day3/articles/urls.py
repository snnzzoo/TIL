from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),  # '': 홈페이지
    path('create/', views.create, name='create'),
]
