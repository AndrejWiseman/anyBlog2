from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include

from posts.views import home, post_detail, search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('post/<int:id>/', post_detail, name='post-detail'),
    path('search/', search, name='search'),
    path('tinymce/', include('tinymce.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
