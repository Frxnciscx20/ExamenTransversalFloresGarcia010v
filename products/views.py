from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Products
from django.views.generic.detail import DetailView
from django.db.models import Q

class ProductListView(ListView):
    template_name = 'productos.html'
    queryset = Products.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['mensaje'] = 'Productos'

        return context



class ProductDetailView(DetailView):
    model = Products
    template_name = 'products/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

class ProductSearchListView(ListView):
    template_name = 'products/search.html'

    def get_queryset(self):
        filters = Q(title__icontains=self.query()) | Q(category__title__icontains=self.query())
        return Products.objects.filter(filters)


    def query(self):
        return self.request.GET.get('i')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['query'] = self.query()

        return context