from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.urls import reverse_lazy
from .models import Product, Category


class HomeView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'
    paginate_by = 2


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'create_product.html'
    fields = ['name', 'description', 'image', 'category', 'price']
    success_url = reverse_lazy('home')


class ContactsView(TemplateView):
    template_name = 'contacts.html'