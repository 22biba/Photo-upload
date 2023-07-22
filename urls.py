from django.urls import path, include
from django.contrib import admin
from photos import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # URL pattern for the admin site
    path('', include('photos.urls')),  # URL pattern for the 'photos' app
]

# Configure static and media file serving during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
