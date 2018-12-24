from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import myProducts
from .forms import ProductCreation, ProductEdit
import datetime

# Create your views here.

def index(request):
    products = myProducts.objects.all()
    context = {'Product': products}
    return render(request, 'products/dashboard.html', context)


def Create(request):
    if request.method == 'POST':
        form = ProductCreation(request.POST)
        if form.is_valid():
            new_product = myProducts(ProductTitle=request.POST['pName'],
            Description=request.POST['pDesciption'],
            Objectives=request.POST['pObjectives'],
            Vision=request.POST['pVision'],
            SubmissionDate=datetime.datetime.now()
            )
            new_product.save()
            return redirect('index')
        else:
            form = ProductCreation()

    form = ProductCreation()
    context = {'form': form}
    return render(request, 'products/products.html', context)


def Delete(request, pk):
    entry = get_object_or_404(myProducts, pk=pk)
    entry.delete()
    return HttpResponseRedirect('/')


def Edit(request, pk):
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
