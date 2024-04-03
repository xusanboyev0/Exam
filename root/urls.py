from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# from apps.urls import urlpatterns

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path("", include('apps.urls')),
                  path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
