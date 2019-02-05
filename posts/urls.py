from django.urls import path
from . import views

urlpatterns = [
    path('', views.post, name = 'post'),
    path('<str:account>/', views.mypage, name = 'page'),
    path('create/', views.create, name = 'post_create'),
    path('update/', views.update, name = 'post_update'),
    path('delete/', views.delete, name = 'post_delete'),
]