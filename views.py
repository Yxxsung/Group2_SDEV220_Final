
from django.shortcuts import render, redirect
from .models import Product, CartItem
 
 #brings up a list of products from the database and renders a template in order to display them.
 #Should show name, price, and an add to cart button
def product_list(request):
    products = Product.objects.all()
    return render(request, 'myapp/index.html', {'products': products})
 

 #Displays the contents of the shopping cart according to current user, calculates the total, and renders
 #a template to display the cart and price
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'myapp/cart.html', {'cart_items': cart_items, 'total_price': total_price})
 

 #triggered when add to cart is clicked. takes items id as a parameter, retrieves the corressponding cart item and adds it to the database.
 #also increments quantity and redirects user to the cart view.
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, 
                                                       user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart:view_cart')
 

 #removes an item and updates the cart to show the correct items and total
def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('cart:view_cart')
 
 

 #returns to home
def home(request):
    return HttpResponse('Hello, World!')
