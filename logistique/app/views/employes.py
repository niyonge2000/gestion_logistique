from django.shortcuts import redirect,render
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from app.models import Employe
from app.form import EmployeForm

@login_required(login_url='/login')
def index(request):
    employes = Employe.objects.all()
    #assert isinstance(request, HttpRequest)
    return render(
        request, 
        'app/employes/index.html',
        {
            'employes': employes
        }
    )

@login_required(login_url='/login')
def add(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        form = EmployeForm
    return render(
        request,
        'app/employes/add.html',
        {
        'form': form
        }
    )

@login_required(login_url='/login')
def store(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        form = EmployeForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('/employes')

@login_required(login_url='/login')
def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if id == 0:
            form = EmployeForm()
        else:
            employes = Employe.objects.get(pk=id)
            form = EmployeForm(instance=employes)
        return render(
            request, 
            'app/employes/edit.html', 
            {
                'form':form
            }

        )

@login_required(login_url='/login')
def update(request, id):
     assert isinstance(request, HttpRequest)
     if request.method == 'POST':
        if id == 0:
            form = EmployeForm(request.POST)
        else:
            employes = Employe.objects.get(pk=id)
            form = EmployeForm(request.POST, instance=employes)
        if form.is_valid():
            form.save()        
     return redirect('/employes')

@login_required(login_url='/login')
def delete(request,id):
    employes = Employe.objects.get(pk=id)
    employes.delete()
    return redirect('/employes')
            