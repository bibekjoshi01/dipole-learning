from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),

    #apps urls
    path('', include('core_app.urls')),
    path('blog/', include('blog.urls')),
    path('api/', include('api.urls')),

    #jwt urls
    path('api/token', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('api/token/refresh', TokenRefreshView.as_view(), name="token_refresh"),

    #rest_framework urls
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


