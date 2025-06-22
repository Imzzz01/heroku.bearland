// Function to handle adding to cart with AJAX
function addToCart(productId, quantity = 1) {
    fetch(`/cart/add/${productId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
            'Content-Type': 'application/json',
            'X-Requested-With': 'XMLHttpRequest'
        },
        body: JSON.stringify({quantity: quantity})
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            Swal.fire({
                title: 'Success!',
                text: data.message,
                icon: 'success',
                timer: 2000,
                showConfirmButton: false
            });
            // Update cart count if needed
            updateCartCount();
        }
    })
    .catch(error => {
        Swal.fire({
            title: 'Error!',
            text: 'Could not add item to cart',
            icon: 'error'
        });
    });
}

// Function to update cart count display
function updateCartCount() {
    fetch('/cart/count/')
    .then(response => response.json())
    .then(data => {
        if (data.count !== undefined) {
            document.querySelector('.cart-count').textContent = data.count;
        }
    });
}

// Quick add to cart function
function quickAddToCart(productId) {
    addToCart(productId, 1);
}

// Add to wishlist function
function addToWishlist(productName) {
    Swal.fire({
        title: 'Added to Wishlist!',
        text: `${productName} has been added to your wishlist`,
        icon: 'success',
        timer: 2000,
        showConfirmButton: false
    });
}

// Initialize functions when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Initialize AOS for animations
    AOS.init();
    
    // Add floating animation to related product cards
    const cards = document.querySelectorAll('.related-product-card');
    cards.forEach((card, index) => {
        card.style.animationDelay = `${index * 0.1}s`;
        card.classList.add('animate-fade-in');
    });
});