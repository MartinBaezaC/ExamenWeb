from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout as auth_logout
from django.http import HttpResponse


def cargarInicio(request):
    return render(request, 'aplicacion/index.html')

def cargarLogin(request):
	return render(request, 'aplicacion/cargar-login.html')


def logout(request):
    """Logs out user"""
    auth_logout(request)
    return render(request, 'aplicacion/index.html')

@login_required
def cargarOrden(request):
	return render(request, 'aplicacion/cargar-orden.html')


@login_required
def cargarListado(request):
	return render(request, 'aplicacion/cargar-listado.html')