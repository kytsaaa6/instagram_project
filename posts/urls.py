from django.urls import path
from . import views

urlpatterns = [
    path('', views.post, name='post'),
    path('<str:account>/', views.my_page, name='post_mypage'),
    path('<str:account>/create/', views.create, name='post_create'),
    path('<int:post_id>/update/', views.update, name='post_update'),
    path('<int:post_id>/delete/', views.delete, name='post_delete'),
    path('<int:post_id>/like/', views.post_like, name='post_like')
]