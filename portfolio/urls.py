from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from api.views import portfolio_index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),

    # Serve individual side projects at /projects/<slug>/
    path('projects/', include('projects.urls')),

    # Main portfolio landing page
    path('', portfolio_index, name='index'),
]

# Serve static and media files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
