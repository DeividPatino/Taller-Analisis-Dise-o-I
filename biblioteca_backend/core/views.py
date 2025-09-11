from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .models import Usuario, Libro, Reserva, Prestamo
from .serializers import UsuarioSerializer, LibroSerializer, ReservaSerializer, PrestamoSerializer
from django.shortcuts import render


# =====================
# Vistas Frontend (HTML)
# =====================

def login_page(request):
    return render(request, "login.html")

def registro_page(request):
    return render(request, "registro.html")

def catalogo_page(request):
    return render(request, "catalogo.html")

def historial_page(request):
    return render(request, "historial.html")



# =====================
# API (JSON / Backend)
# =====================

# Login API
@api_view(['POST'])
def login(request):
    username = request.data.get("usuario")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)
    if user:
        serializer = UsuarioSerializer(user)
        return Response(serializer.data)
    return Response({"error": "Credenciales inválidas"}, status=status.HTTP_401_UNAUTHORIZED)

# Registrar usuario API
@api_view(['POST'])
def registrar_usuario(request):
    username = request.data.get("usuario")
    password = request.data.get("password")
    rol = request.data.get("rol", "estudiante")

    if Usuario.objects.filter(username=username).exists():
        return Response({"error": "Usuario ya existe"}, status=400)

    user = Usuario.objects.create_user(username=username, password=password, rol=rol)
    serializer = UsuarioSerializer(user)
    return Response(serializer.data)

# Buscar libros API
@api_view(['GET'])
def buscar_libros(request):
    query = request.GET.get("titulo", "")
    libros = Libro.objects.filter(titulo__icontains=query)
    serializer = LibroSerializer(libros, many=True)
    return Response(serializer.data)

# Reservar libro API
@api_view(['POST'])
def reservar_libro(request):
    usuario_id = request.data.get("usuarioId")
    libro_id = request.data.get("libroId")

    libro = Libro.objects.get(id=libro_id)
    if not libro.disponible:
        return Response({"error": "Libro no disponible"}, status=400)

    reservas_usuario = Reserva.objects.filter(usuario_id=usuario_id).count()
    if reservas_usuario >= 5:
        return Response({"error": "Máximo 5 reservas"}, status=400)

    libro.disponible = False
    libro.save()

    reserva = Reserva.objects.create(usuario_id=usuario_id, libro_id=libro_id)
    serializer = ReservaSerializer(reserva)
    return Response(serializer.data)
