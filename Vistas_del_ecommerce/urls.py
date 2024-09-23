from django.contrib import admin
from django.urls import path, include
from ventas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.lista_productos, name='home'),  # Cambia 'product_list' por 'lista_productos'
    path('ventas/', include('ventas.urls')),  # Incluir las URLs de la aplicación 'ventas'
]
