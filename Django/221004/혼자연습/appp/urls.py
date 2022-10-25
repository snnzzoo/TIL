from django.urls import path
from . import views

app_name = 'appp'

urlpatterns = [
    path('', views.index, name='index'),
]
