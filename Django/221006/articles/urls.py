from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    # http://127.0.0.1:8000/articles/
    path('', views.index, name="index"),
    # http://127.0.0.1:8000/articles/create/
    path('create/', views.create, name="create"),
    # http://127.0.0.1:8000/articles/1/ : 1번 글
    # http://127.0.0.1:8000/articles/3/ : 3번 글
    path('<int:pk>/', views.detail, name="detail"),
    # http://127.0.0.1:8000/articles/1/update/ : 1번 글 수정
    # http://127.0.0.1:8000/articles/3/update/ : 3번 글 수정
    path('<int:pk>/update/', views.update, name="update"),
    # http://127.0.0.1:8000/articles/1/delete : 1번 글 삭제
    # http://127.0.0.1:8000/articles/3/delete : 3번 글 삭제
    path('<int:pk>/delete/', views.delete, name="delete"),
]