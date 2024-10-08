from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('usersapp.urls')),
    path('chat/', include('chatapp.urls')),  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "chatapp.views.custom_404"