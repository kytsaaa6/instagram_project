from django.urls import path
from . import views

urlpatterns = [
    path('<int:post_id>/comment/', views.comment, name='comment'),
    path('<int:comment_id>/comment/delete/', views.comment_delete, name='comment_delete'),
]