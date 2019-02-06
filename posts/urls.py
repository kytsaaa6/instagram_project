from django.urls import path
from . import views

urlpatterns = [
    path('', views.post, name = 'post'),
    path('<str:username>/', views.mypage, name = 'mypage'),
    path('create/go/', views.create, name = 'post_create'),
    path('update/', views.update, name = 'post_update'),
    path('delete/', views.delete, name = 'post_delete'),
]