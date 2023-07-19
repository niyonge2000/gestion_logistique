
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from app.models import Product
from app.form import ProductForm

@login_required(login_url='/login')
def index(request):
    assert isinstance(request, HttpRequest)
    products = Product.objects.all()
    return render(
        request,
        'app/products/index.html',
        {
            'products': products
        }
    )

@login_required(login_url='/login')    
def create(request):
    form = ProductForm()
    return render(
        request, 
        'app/products/add.html',
        {
            'form': form
        }
    )

@login_required(login_url='/login') 
def store(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, "Product has been saved successfully !")
        return redirect('/products')

@login_required(login_url='/login')    
def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = ProductForm()
        else:
            product = Product.objects.get(pk=id)
            form = ProductForm(instance=product)
        return render(
            request,
            'app/products/edit.html',
            {
                'form': form
            }
        )
    else:
        if id == 0:
            form = ProductForm(request.POST)
        else:
            product = Product.objects.get(pk=id)
            form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
        messages.success(request, "Product has been updated successfully !")
        return redirect('/products')

@login_required(login_url='/login')   
def delete(request, id):
    product = Product.objects.get(pk=id)
    product.delete()
    messages.success(request, "Product has been removed successfully !")
    return redirect('/products')