from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    # http://127.0.0.1:8000/articles/
    path('', views.index, name="index"),
    # http://127.0.0.1:8000/articles/new/
    # path('new/', views.new, name="new"),
    # http://127.0.0.1:8000/articles/create/
    path('create/', views.create, name="create"),
    # # http://127.0.0.1:8000/articles/10/
    path('<int:pk>/', views.detail, name="detail"),
]
