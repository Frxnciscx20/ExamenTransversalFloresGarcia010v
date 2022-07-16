from django.shortcuts import render
from .models import Cart
from products.models import Products
from .funciones import funcionCarrito
from django.shortcuts import redirect
from .models import CartProduct


def cart(request):
    cart = funcionCarrito(request)
    return render(request, 'carts/cart.html', {
        'cart': cart
    })

def add(request):
    cart = funcionCarrito(request)
    product = Products.objects.get(pk=request.POST.get('product_id'))
    quantity = int(request.POST.get('quantity', 1))

    #cart.products.add(product, through_default={
    #    'quantity': quantity
    #})

    product_cart = CartProduct.objects.crearActualizar(cart=cart, product=product, quantity=quantity)

    return render(request, 'carts/add.html',{
        'product': product
    })

def remove(request):
    cart = funcionCarrito(request)
    product = Products.objects.get(pk=request.POST.get('product_id'))

    cart.products.remove(product)
    return redirect('cart')