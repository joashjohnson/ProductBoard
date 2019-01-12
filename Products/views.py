from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import myProducts
from .forms import ProductCreation, ProductEdit
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def index(request):
    products = myProducts.objects.all().filter(ProductAccessList=request.user)
    context = {'Product': products}
    return render(request, 'products/dashboard.html', context)

@login_required
def Create(request):
    if request.method == 'POST':
        form = ProductCreation(request.POST)
        if form.is_valid():
            new_product = myProducts(ProductTitle=request.POST['pName'],
            Description=request.POST['pDesciption'],
            Objectives=request.POST['pObjectives'],
            Vision=request.POST['pVision'],
            SubmissionDate=datetime.datetime.now(),
            )
            new_product.save()
            return redirect('index')
        else:
            form = ProductCreation()
    form = ProductCreation()
    context = {'form': form}
    return render(request, 'products/products.html', context)

@login_required
def Delete(request, pk):
    entry = get_object_or_404(myProducts, pk=pk)
    entry.delete()
    return HttpResponseRedirect('/')

@login_required
def Edit(request, pk):
    # update does not work for product access list
    entry = get_object_or_404(myProducts, pk=pk)
    if request.method == "POST":
        form = ProductEdit(request.POST, instance = entry)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.save()
            return redirect('index')
            # Save was successful, so redirect to another page
    else:
        form = ProductEdit(instance=entry)
    return render(request, 'products/productedit.html', context = {'form': form , 'entry':entry})

@login_required
def AccessChecker(request):
    return redirect('index')
