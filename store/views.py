from django.shortcuts import render
from .models import Product, Gift
# Create your views here.

def home(request):
    return render(request, 'store/home.html')

def products(request):
    products = Product.objects.filter(is_gift=False)
    return render(request, 'store/product.html', {'products': products})

def gifts(request):
    gifts = Gift.objects.all()
    return render(request, 'store/gifts.html', {'gifts': gifts})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})

def search(request):
    query = request.GET.get('q')
    results = Product.objects.filter(name__icontains=query) if query else []
    return render(request, 'store/search_results.html', {'results': results, 'query': query})