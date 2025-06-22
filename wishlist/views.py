# wishlist/views.py
#from django.shortcuts import render, get_object_or_404
#from django.contrib.auth.decorators import login_required
#from django.http import JsonResponse
#from wishlist.models import Wishlist, WishlistItem
#from store.models import Product

#@login_required
#def wishlist_view(request):
 #   wishlist, created = Wishlist.objects.get_or_create(user=request.user)
  #  wishlist_items = wishlist.wishlistitem_set.select_related('product').all()
   # return render(request, 'wishlist/wishlist.html', {'wishlist_items': wishlist_items})

#@login_required
#def add_to_wishlist(request, product_id):
  #  if request.method == 'POST':
    #    product = get_object_or_404(Product, id=product_id)
    #    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
        
       # if not WishlistItem.objects.filter(wishlist=wishlist, product=product).exists():
         #   WishlistItem.objects.create(wishlist=wishlist, product=product)
          #  return JsonResponse({'success': True, 'action': 'added', 'count': wishlist.products.count()})
        #return JsonResponse({'success': False, 'message': 'Product already in wishlist'})
    #return JsonResponse({'success': False, 'message': 'Invalid request'})

#@login_required
#def remove_from_wishlist(request, item_id):
 #   if request.method == 'POST':
  #      try:
   #         item = get_object_or_404(WishlistItem, id=item_id, wishlist=request.user.wishlist)
    #        item.delete()
     #       return JsonResponse({'success': True, 'action': 'removed', 'count': request.user.wishlist.products.count()})
      #  except Exception as e:
      #      return JsonResponse({'success': False, 'message': str(e)})
    #return JsonResponse({'success': False, 'message': 'Invalid request'})