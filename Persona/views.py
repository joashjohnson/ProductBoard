from .models import user_persona
from Products.models import myProducts
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth.models import User



listing = "no"
# Create your views here.
@login_required
def pindex(request):
    persona = user_persona.objects.all().filter(PProduct__ProductAccessList=request.user)
    context = {'Persona': persona}
    return render(request, 'persona/persona.html', context)

@login_required
def create_persona(request):
    if request.method == 'POST':
        form = PersonaCreation(request.user, request.POST, request.FILES or None)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.save()
        return redirect('pindex')
    else:
        form = PersonaCreation(request.user)
    return render(request, 'persona/createpersona.html', context={'form': form})
@login_required
def del_persona(request,pk):
    entry = get_object_or_404(user_persona, pk=pk)
    entry.delete()
    return redirect('pindex')

@login_required
def edit_persona(request,pk):
    entry = get_object_or_404(user_persona, pk=pk)
    if request.method == "POST":
        form = PersonaEdit(request.user, request.POST,request.FILES or None, instance = entry)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.save()
            return redirect('pindex')
    else:
        form = PersonaEdit(request.user,instance=entry)
    return render(request, 'persona/editpersona.html', context={'form': form, 'entry':entry})

@login_required
def product_persona(request,fk):
    listing = "yes"
    currentf = fk
    persona = user_persona.objects.all().filter(PProduct__ProductAccessList=request.user)
    context = {'Persona': persona, 'fk' : currentf, 'Listing': listing}
    return render(request, 'persona/persona.html', context)
