<div>
		<h1>Sharboard Heights Store</h1>
	</div>




<h1>Your Shopping Cart</h1>

	<div class="product-list">

	


	<div class="product-item">
		<p></p> ({{ item.quantity }})</p>
		<p>Price: ${{ item.product.price }}</p>
		<a href="{% url 'cart:remove_from_cart' item.id %}">Remove</a>
	</div>
	<p>Your cart is empty.</p>

	</div>

	<p>Total Price: ${{ total_price }}</p>

	<a href="{% url 'cart:product_list' %}">Continue Shopping</a>