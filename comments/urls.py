from django.urls import path
from . import views


urlpatterns = [
    path('<pk>/comment/', views.comment_create, name = 'comment_create'),
    path('<pk>/comment/delete/', views.comment_delete, name = 'comment_delete'),
]
