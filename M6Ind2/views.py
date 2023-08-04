from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UsuarioForm
from .models import Usuario
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def landing(request):
    return render(request, 'M6Ind2/landing.html')

def clientes(request):
    usuarios = Usuario.objects.all()
    contexto = {'usuarios': usuarios}
    return render(request, 'M6Ind2/usuarios.html', contexto)

def createUsuario(request):
    if request.method == "POST":
        formulario_post = UsuarioForm(request.POST)
        if formulario_post.is_valid():
            formulario_post.save()
            messages.success(request, 'Usuario creado exitosamente.')
            return redirect(createUsuario)
        else:
            messages.error(request, 'Ha ocurrido un error al crear el usuario. Por favor, verifica los datos ingresados.')

    formulario_get = UsuarioForm()
    return render(request, 'M6ind2/registro.html', {'formulario': formulario_get})

   