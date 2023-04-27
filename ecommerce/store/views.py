from django.shortcuts import render
from .models import Product
# .models because we have the Product models in the same store app

# Create your views here.
def store(request):
    products = Product.objects.all().filter(is_available=True)
    product_count =  products.count()

    context = {
        'products': products,
        'product_count': product_count,
    }
    # context will make this available for the html page

    return render(request, 'store/store.html', context)
