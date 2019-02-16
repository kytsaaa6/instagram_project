from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    path('signup/', views.signup, name='signup' ),
    path('signup_ok/', TemplateView.as_view(template_name='registration/signup_ok.html'), name='signup_ok'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('<str:account>/follow/', views.follow, name='follow'),

]