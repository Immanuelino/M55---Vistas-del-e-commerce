from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Pedido, PedidoProducto

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'ventas/ventas.html', {'productos': productos})

def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito = request.session.get('carrito', {})
    
    if str(producto.id) not in carrito:
        carrito[str(producto.id)] = {
            'nombre': producto.nombre,
            'precio': float(producto.precio),
            'cantidad': 1
        }
    else:
        carrito[str(producto.id)]['cantidad'] += 1
    
    request.session['carrito'] = carrito
    return redirect('lista_productos')

def eliminar_del_carrito(request, producto_id):
    carrito = request.session.get('carrito', {})
    
    if str(producto_id) in carrito:
        del carrito[str(producto_id)]
    
    request.session['carrito'] = carrito
    return redirect('lista_productos')

def procesar_pedido(request):
    carrito = request.session.get('carrito', {})
    total = sum(float(item['precio']) * item['cantidad'] for item in carrito.values())
    
    # Aquí podrías crear un pedido en la base de datos
    pedido = Pedido(cliente='Cliente Anónimo', total=total)  # Cambia esto según tu lógica
    pedido.save()

    for item in carrito.values():
        pedido_producto = PedidoProducto(
            pedido=pedido,
            producto=get_object_or_404(Producto, nombre=item['nombre']),
            cantidad=item['cantidad'],
            precio=item['precio']
        )
        pedido_producto.save()
    
    # Limpiar el carrito
    request.session['carrito'] = {}
    
    return render(request, 'ventas/pedido_confirmado.html', {'total': total})


def modificar_cantidad_carrito(request, producto_id):
    carrito = request.session.get('carrito', {})
    
    if str(producto_id) in carrito:
        nueva_cantidad = int(request.POST.get('cantidad', 1))  # Obtiene la nueva cantidad del formulario
        if nueva_cantidad > 0:
            carrito[str(producto_id)]['cantidad'] = nueva_cantidad
        else:
            del carrito[str(producto_id)]  # Elimina el producto si la cantidad es 0
    
    request.session['carrito'] = carrito
    return redirect('lista_productos')
