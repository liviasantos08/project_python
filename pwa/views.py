from django.shortcuts import render, redirect
from .models import Product, Entrega
from .forms import ProductForm
from rest_framework import viewsets
from .serializers import EntregSerie


def base(request):

    return render(request, 'base.html')


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product-list')
        
    else:
        form = ProductForm()

    return render(request, 'product_create.html', {'form': form})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


class EntregList(viewsets.ModelViewSet):
    queryset = Entrega.objects.all()
    serializer_class = EntregSerie


