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