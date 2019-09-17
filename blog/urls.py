from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('myblog/', views.myblog, name='myblog'),
    path('search/', views.search, name='search'),
    path('user/<id>/', views.blog, name='blog'),
    path('post/<id>/', views.post, name='post'),
    path('createpost/', views.create_post, name='create_post'),
    path('create/', views.create_blog, name='create_blog'),
    path('edit/<id>/', views.edit_blog, name='edit_blog'),
    path('delete/<id>/', views.delete_blog, name='delete_blog'),
    path('post/delete/<id>/', views.delete_post, name='delete_post'),
    path('post/edit/<id>/', views.edit_post, name='edit_post'),
    path('follow/<id>/', views.follow, name='follow'),
    path('following/', views.following, name='following'),
    path('followers/', views.followers, name='followers'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
