from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from posts import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.post, name='posts_post'),
    path('posts/', include('posts.urls')),
    path('account/', include('accounts.urls')),
    path('comments/', include('comments.urls')),
    path('explore/', views.explore, name='explore'),
    path('explore/tags/<str:tag>/', views.tag_list, name='post_tag'),
    path('search/', views.search, name='search'),
    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

