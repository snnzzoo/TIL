from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    # http://127.0.0.1:8000/movies/
    path('', views.index, name="index"),
    # http://127.0.0.1:8000/movies/create/
    path('create/', views.create, name="create"),
    # http://127.0.0.1:8000/movies/3/ : 3번 글
    path('<int:pk>/', views.detail, name="detail"),
    # http://127.0.0.1:8000/movies/3/update/ : 3번 글 수정
    path('<int:pk>/update/', views.update, name="update"),
    # http://127.0.0.1:8000/movies/3/delete/ : 3번 글 삭제
    path('<int:pk>/delete/', views.delete, name="delete"),
]