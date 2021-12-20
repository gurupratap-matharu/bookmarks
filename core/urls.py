from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Django admin
    path("dj-admin/", admin.site.urls),
    # User management
    path("accounts/", include("allauth.urls")),
    # Local
    path("", include("pages.urls")),
    path("profile/", include("users.urls")),
    path("images/", include("images.urls", namespace="images")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
