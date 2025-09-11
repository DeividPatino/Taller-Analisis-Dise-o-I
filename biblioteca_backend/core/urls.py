from django.urls import path
from . import views

urlpatterns = [
    # Frontend (HTML)
    path("login", views.login_page, name="login_page"),
    path("registro", views.registro_page, name="registro_page"),
    path("adminpanel", views.admin_panel, name="admin_panel"),
    path("catalogo", views.catalogo_page, name="catalogo_page"),
    path("historial", views.historial_page, name="historial_page"),

    # API
    path("api/login/", views.login, name="api_login"),
    path("api/usuarios/", views.registrar_usuario, name="api_registrar_usuario"),
    path("api/libros/", views.buscar_libros, name="api_buscar_libros"),
    path("api/reservas/", views.reservar_libro, name="api_reservar_libro"),
]
