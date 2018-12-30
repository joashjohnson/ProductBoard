from .models import user_persona
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.core.files.storage import FileSystemStorage

# Create your views here.

def pindex(request):
    persona = user_persona.objects.all()
    context = {'Persona': persona}
    return render(request, 'persona/persona.html', context)


def create_persona(request):
    if request.method == 'POST':
        form = PersonaCreation(request.POST, request.FILES or None)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.save()
            fs = FileSystemStorage()
            fs.save(entry,'Picmage')
            return redirect('pindex')
    else:
        form = PersonaCreation()

    return render(request, 'persona/createpersona.html', context={'form': form})

def del_persona(request,pk):
    entry = get_object_or_404(user_persona, pk=pk)
    entry.delete()
    return redirect('pindex')


def edit_persona(request,pk):
    entry = get_object_or_404(user_persona, pk=pk)
    if request.method == "POST":
        form = PersonaEdit(request.POST,request.FILES or None, instance = entry)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.save()
            return redirect('pindex')
    else:
        form = PersonaEdit(instance=entry)
    return render(request, 'persona/editpersona.html', context={'form': form, 'entry':entry})


