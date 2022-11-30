from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('users.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
