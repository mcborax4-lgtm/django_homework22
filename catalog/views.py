from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from .models import Product, Category
from .forms import ProductForm
from .services import get_products_by_category, get_cached_products


class HomeView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'
    paginate_by = 2

    def get_queryset(self):
        return get_cached_products()


@method_decorator(cache_page(60), name='dispatch')
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'create_product.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'create_product.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.owner


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        product = self.get_object()
        return (self.request.user == product.owner or
                self.request.user.has_perm('catalog.delete_product'))


class ContactsView(TemplateView):
    template_name = 'contacts.html'


class ProductByCategoryView(LoginRequiredMixin, ListView):
    template_name = 'products_by_category.html'
    context_object_name = 'products'

    def get_queryset(self):
        return get_products_by_category(self.kwargs['category_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

