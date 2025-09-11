from django.shortcuts import render

def index_page(request):
    return render(request, "index.html")

def login_page(request):
    return render(request, "login.html")

def registro_page(request):
    return render(request, "registro.html")

def catalogo_page(request):
    return render(request, "catalogo.html")

def historial_page(request):
    return render(request, "historial.html")