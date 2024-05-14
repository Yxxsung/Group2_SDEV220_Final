
var addItemId = 0;

function addToCart(item)
{
    addItemId += 1;
    var selectedItem=document.createElement('div');
    selectedItem.classList.add('cartImg');
    selectedItem.setAttribute('id',addItemId);
    var cartItems = document.getElementByID('title');
    cartItems.append(selectedItem);
}

