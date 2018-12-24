from django.shortcuts import render
from .models import user_persona
from django.shortcuts import render

# Create your views here.

def pindex(request):
    persona = user_persona.objects.all()
    context = {'Persona': persona}
    return render(request, 'persona/persona.html', context)