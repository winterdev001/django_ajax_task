from django.urls import path, include
from . import views
 
urlpatterns = [
    path('blogs/', views.index, name='index'),
    path('blogs/create', views.create, name='create'),
    path('blogs/detail/<int:blog_id>', views.detail, name='detail'),
    path('blogs/edit/<int:blog_id>', views.edit, name='edit'),
    path('blogs/delete/<int:blog_id>',views.delete, name='delete'),
    path('blogs/like/<int:blog_id>',views.blogLike, name= 'blog_like'),
]