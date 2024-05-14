
var addItemId = 0;

function addToCart(item)
{
    addItemId += 1;
    var selectedItem=document.createElement('div');
    selectedItem.classList.add('cartImg');
    selectedItem.setAttribute('id',addItemId);
    var img = document.createElement('img');
    img.setAttribute('src', item.children[0].currentSrc);
    var title = document.createElement('div');
    title.innerText = item.children[1].innerText;
    var label = document.createElement('div');
    label.innerText = item.children[2].children[0].innerText;
    var select = document.createElement('span');
    var cartItems = document.getElementByID('title');
    selectedItem.append(img);
    cartItems.append(selectedItem);
}

