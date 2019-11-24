from django.shortcuts import render, get_object_or_404
from .models import Product
from django.views.generic import ListView

class ProductListView(ListView):
    queryset = Product.objects.all()
    context_object_name = 'products'
    paginate_by = 2
    template_name = 'blog/product/list.html'


def product_list(request):
    products = Product.objects.all()
    return render(request, 'blog/product/list.html',
                  {'products': products})

def product_detail(request, y, month, day, product):
    product = get_object_or_404(Product, slug=product,
                             status='published',
                             publish__year=y,
                             publish__month=month,
                             publish__day=day)
    return render(request, 'blog/post/detail.html',
                  {'product':product})