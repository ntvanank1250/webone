from django.urls import path
from . import views

app_name="main"
urlpatterns = [
    path('', views.home, name='home'),
    path('1', views.first, name='first'),
    path('2', views.second, name='second'),
    path('3', views.third, name='third'),
]