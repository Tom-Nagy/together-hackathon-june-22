''' connect_with URL Configuration '''

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


# for media option
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('chatrooms/', include('chatrooms.urls')),
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
