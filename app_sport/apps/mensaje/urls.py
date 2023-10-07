from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from .views import *

app_name = 'apps.mensaje'
urlpatterns = [
    path('enviar_mensaje/', enviar_mensaje, name='enviar_mensaje'),
    path('ver_mensajes/', ver_mensajes, name='ver_mensajes'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
