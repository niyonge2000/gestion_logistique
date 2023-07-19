from django.shortcuts import redirect,render
from django.http import HttpRequest
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app.models import Category
from app.form import CategoryForm

@login_required(login_url='/login')
def index(request):
    categories = Category.objects.all()
    #assert isinstance(request, HttpRequest)
    return render(
        request, 
        'app/categories/index.html',
        {
            'categories': categories
        }
    )

@login_required(login_url='/login')
def add(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        form = CategoryForm
    return render(
        request,
        'app/categories/add.html',
        {
        'form': form
        }
    )

# Ajouter un nouveau categorie
@login_required(login_url='/login')
def store(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
    messages.success(request, "Category has been saved successfully !")
    return redirect('/categories')

@login_required(login_url='/login')
def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if id == 0:
            form = CategoryForm()
        else:
            category = Category.objects.get(pk=id)
            form = CategoryForm(instance=category)
        return render(
            request, 
            'app/categories/edit.html', 
            {
                'form':form
            }

        )

@login_required(login_url='/login')
def update(request, id):
     assert isinstance(request, HttpRequest)
     if request.method == 'POST':
        if id == 0:
            form = CategoryForm(request.POST)
        else:
            category = Category.objects.get(pk=id)
            form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "Category has been updated successfully !")        
     return redirect('/categories')

@login_required(login_url='/login')     
def delete(request,id):
    category = Category.objects.get(pk=id)
    category.delete()
    messages.success(request, "Category has been removed successfully !")
    return redirect('/categories')
            