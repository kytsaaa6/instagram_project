from django.urls import path
from . import views

urlpatterns = [
    path('<pk>/comment/', views.comment_create, name = 'comment_create'),
#    path('create/go/', views.create, name = 'post_create'),
#    path('<pk>/update/', views.update, name = 'post_update'),
    path('<pk>/comment/delete/', views.comment_delete, name = 'comment_delete'),
]