from django.urls import path
from . import views

app_name="blog"
urlpatterns = [
   
    path('', views.blog, name='blog'),
    path('create-blog/', views.create_blog, name='create_blog'),
    path('update-blog/<int:id>/', views.update_blog, name='update_blog'),
    path('delete-blog/<int:id>/', views.delete_blog, name='delete_blog'),
    path('<int:id>/', views.blog_i, name='blog_i'),
]
