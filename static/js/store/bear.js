function addToCart(productId, price) {
    const csrfToken = document.querySelector('meta[name="csrf-token"]').content;
    
    fetch(`/cart/add/${productId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrfToken,
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            price: price,
            quantity: 1
        })
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(err => { 
                throw new Error(err.message || 'Failed to add to cart'); 
            });
        }
        return response.json();
    })
    .then(data => {
        if (data.success) {
            Swal.fire({
                title: 'Success!',
                text: data.message,
                icon: 'success',
                timer: 2000,
                showConfirmButton: false
            });
            updateCartCount(data.item_count);
        }
    })
    .catch(error => {
        Swal.fire({
            title: 'Error!',
            text: error.message.includes('login') ? 
                  'Please login to add items to cart' : 
                  'Could not add item to cart',
            icon: 'error'
        });
        if (error.message.includes('login')) {
            window.location.href = '/accounts/login/?next=' + window.location.pathname;
        }
    });
}

function updateCartCount(count) {
    const cartCountElements = document.querySelectorAll('.cart-count');
    cartCountElements.forEach(el => {
        el.textContent = count;
    });
}

function addToWishlist(productId) {
    fetch(`/wishlist/add/${productId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
            'Content-Type': 'application/json',
        },
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            Swal.fire({
                title: 'Added to Wishlist!',
                text: 'Product has been added to your wishlist',
                icon: 'success',
                timer: 2000,
                showConfirmButton: false
            });
            updateWishlistCount(data.count);
        } else {
            Swal.fire({
                title: 'Already in Wishlist',
                text: data.message,
                icon: 'info',
                timer: 2000,
                showConfirmButton: false
            });
        }
    });
}

function updateWishlistCount(count) {
    const wishlistCount = document.getElementById('wishlist-count');
    if (wishlistCount) {
        wishlistCount.textContent = count;
        if (count > 0) {
            wishlistCount.style.display = 'inline-block';
        } else {
            wishlistCount.style.display = 'none';
        }
    }
}