from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api-auth/', include('rest_framework.urls')),
                  path('api/v1/', include('api.urls')),
                  path('',
                       TemplateView.as_view(template_name='index.html'),
                       name='uHome'
                       ),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
