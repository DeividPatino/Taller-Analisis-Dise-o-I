from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name='login_page'),
    path('registro/', views.registro_page, name='registro_page'),
    path('catalogo/', views.catalogo_page, name='catalogo_page'),
    path('historial/', views.historial_page, name='historial_page'),
]