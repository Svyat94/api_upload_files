from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from .views import UserViewSet, FileViewSet, upload_file

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'files', FileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('upload/', upload_file, name='upload_file'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
