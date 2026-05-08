from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from django.core.paginator import Paginator

def home(request):
    products_list = Product.objects.all()
    paginator = Paginator(products_list, 2)  # 2 товара на страницу
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    return render(request, 'home.html', {'products': products})

def contacts(request):
    return render(request, 'contacts.html')

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})


def create_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        category_id = request.POST.get('category')
        category = Category.objects.get(pk=category_id)
        Product.objects.create(name=name, description=description, price=price, category=category)
        return redirect('home')

    categories = Category.objects.all()
    return render(request, 'create_product.html', {'categories': categories})