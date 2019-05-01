from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns
from estate import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('estate.urls')),
    path('accounts/', include('estate.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)
