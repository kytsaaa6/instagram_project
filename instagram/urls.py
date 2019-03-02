from django.conf.urls import include
from posts import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    path('account/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('comment/', include('comments.urls')),
    path('explore/post/', views.explore, name='explore'),
    path('explore/tags/<str:tag>/', views.tag_list, name='tag_list'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
