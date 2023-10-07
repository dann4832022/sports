from django.db import models
from django.conf import settings  # Importa settings para obtener el modelo de usuario personalizado

class Mensaje(models.Model):
    remitente = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='mensajes_enviados', on_delete=models.CASCADE)
    destinatario = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='mensajes_recibidos', on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
