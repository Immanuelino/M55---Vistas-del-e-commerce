from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar/<int:producto_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('modificar/<int:producto_id>/', views.modificar_cantidad_carrito, name='modificar_cantidad_carrito'),
    path('procesar/', views.procesar_pedido, name='procesar_pedido'),
]
