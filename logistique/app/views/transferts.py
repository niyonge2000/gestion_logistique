from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from app.models import Transfert, Category, Product
from app.form import TransfertForm

@login_required(login_url='/login')
def index(request):
    assert isinstance(request, HttpRequest)
    transferts = Transfert.objects.all()
    return render(
        request,
        'app/transferts/index.html',
        {
            'transferts': transferts
        }
    )

@login_required(login_url='/login')
def create(request):
    assert isinstance(request, HttpRequest)
    categories = Category.objects.all()
    form = TransfertForm()
    return render(
        request,
        'app/transferts/create.html',
        {
            'form': form,
            'categories': categories
        }
    )

@login_required(login_url='/login')   
def getProducts(request):
    category_id = request.GET.get('category_id')
    products = Product.objects.filter(category_id = category_id).order_by('product_name')
    return render(
        request,
        'app/transferts/getProducts.html',
        {
            'products': products
        }
    )

@login_required(login_url='/login')    
def store(request):
    if request.method == 'POST':
        form = TransfertForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, "Order has been saved successfully !")
        return redirect('/transferts')