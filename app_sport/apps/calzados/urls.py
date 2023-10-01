from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import *

app_name = 'apps.calzados'

urlpatterns = [
    path("agregar_categoria/", AgregarCategoria.as_view(),name='agregar_categoria'),
    path("agregar_calzados/", AgregarCalzados.as_view(), name='agregar_calzados'),
    path("modificar_libro/<int:pk>", ModificarCalzados.as_view(), name='modificar_calzados'),
    path("eliminar_calzados/<int:pk>", EliminarCalzados.as_view(), name='eliminar_calzados'),
    path("listar_calzados/", ListarCalazados.as_view(), name='listar_calzados'),
    # path("libro_detalle/<int:pk>", LibroDetalle.as_view(), name='libro_detalle'),
    path("listar_por_categoria/<str:categoria>",ListarCalzadosPorCategoria, name='listar_por_categoria'),
    # path("libro_detalle/<int:id>", libro_detalle, name='libro_detalle'),
    path("calzados_detalle/<int:id>", calzados_detalle, name='calzados_detalle'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()