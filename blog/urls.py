from django.urls import path
from .import views

urlpatterns = [
    path('myblog/', views.myblog, name='myblog'),
]