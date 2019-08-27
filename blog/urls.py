from django.urls import path
from .import views

urlpatterns = [
    path('myblog/', views.myblog, name='myblog'),
    path('user/<id>/', views.blog, name='blog'),
    path('post/<id>/', views.post, name='post'),
    path('createpost/', views.create_post, name='create_post'),
    path('create/', views.create_blog, name='create_blog'),
    path('edit/<id>/', views.edit_blog, name='edit_blog'),
    path('post/delete/<id>/', views.delete_post, name='delete_post'),
    path('post/edit/<id>/', views.edit_post, name='edit_post'),
]
