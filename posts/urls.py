from django.urls import path
from . import views

urlpatterns = [
    path('', views.post, name='post'),
    path('user/<str:account>/', views.mypage, name='mypage'),
    path('create/', views.create, name='post_create'),
    path('<pk>/update/', views.update, name='post_update'),
    path('<pk>/delete/', views.delete, name='post_delete'),
    path('<pk>/post_like/', views.post_like, name='post_like'),
    path('search/', views.search, name='search'),

]