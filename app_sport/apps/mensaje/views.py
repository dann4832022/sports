from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Mensaje
from apps.usuarios.models import Usuarios
from .forms import MensajeForm

@login_required
def enviar_mensaje(request):
    remitente = request.user

    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            
            # Verifica si el remitente es el superusuario
            if remitente.is_superuser:
                # Si el remitente es el superusuario, selecciona el destinatario de la base de datos.
                destinatario = Usuarios.objects.filter(is_superuser=False).first()
            else:
                # Si el remitente no es el superusuario, establece el destinatario como el superusuario.
                destinatario = Usuarios.objects.filter(is_superuser=True).first()
            
            mensaje.remitente = remitente
            mensaje.destinatario = destinatario
            mensaje.save()
            # Resto de la lógica de redirección o respuesta

            # Resto de la lógica de redirección o respuesta

    form = MensajeForm()
    return render(request, 'mensaje/ver_mensajes.html', {'form': form})


from django.db.models import F
from itertools import chain

@login_required
def ver_mensajes(request):
    mensajes_enviados = Mensaje.objects.filter(remitente=request.user)
    mensajes_recibidos = Mensaje.objects.filter(destinatario=request.user)

    mensajes_enviados = mensajes_enviados.annotate(tipo=F('remitente')).order_by('fecha')
    mensajes_recibidos = mensajes_recibidos.annotate(tipo=F('destinatario')).order_by('fecha')

    mensajes_intercalados = sorted(
        chain(mensajes_enviados, mensajes_recibidos),
        key=lambda mensaje: mensaje.fecha,
        reverse=True
    )

    return render(request, 'mensaje/ver_mensajes.html', {
        'mensajes_intercalados': mensajes_intercalados,
    })

