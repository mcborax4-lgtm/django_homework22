from django.urls import path
from .views import HomeView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, ContactsView, ProductByCategoryView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='create_product'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('category/<int:category_id>/', ProductByCategoryView.as_view(), name='products_by_category'),
]