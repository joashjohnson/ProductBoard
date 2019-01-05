from .models import Ideas
from Products.models import myProducts
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
import sendgrid
import os
from sendgrid.helpers.mail import *
import matplotlib.pyplot as plt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

@login_required
def index_feature(request):
    ideas = Ideas.objects.all().filter(iProduct__ProductAccessList=request.user)
    context =  {
        'Ideas': ideas,
    }
    return render(request, 'features/allideas.html', context)

@login_required
def product_feature(request, fk):
    currentf = fk
    ideas = Ideas.objects.all().filter(iProduct__ProductAccessList=request.user)
    context =  {
        'Ideas': ideas,
        'fk' : currentf,
    }
    return render(request, 'features/list.html', context)

@login_required
def create_feature(request):
    if request.method == 'POST':
        form = FeaturesCreation(request.user, request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.save()
            sendemail()
            return redirect('index_Feature')
    else:
        form = FeaturesCreation(request.user)
    return render(request, 'features/iCreate.html', context={'form': form})

@login_required
def del_feature(request,pk):
    entry = get_object_or_404(Ideas, pk=pk)
    entry.delete()
    return redirect('index_Feature')

@login_required
def edit_feature(request,pk):
        entry = get_object_or_404(Ideas, pk=pk)
        if request.method == "POST":
            form = FeaturesEdit(request.user, request.POST, instance=entry)
            if form.is_valid():
                entry = form.save(commit=False)
                entry.save()
                return redirect('index')
        else:
            form = FeaturesEdit(request.user,instance=entry)
        return render(request, 'features/iedit.html', context={'form': form, 'entry':entry})

@login_required
def view_detail(request,pk,fk):
    currentf = fk
    ideas = get_object_or_404(Ideas, pk=pk)
    context = {
         'ideas': ideas,
         'fk': currentf
    }
    #gengraph(ideas.impact, ideas.effort)
    return render(request, 'features/Detail.html', context)


def sendemail():
    sg = sendgrid.SendGridAPIClient(apikey='1212')
    from_email = Email("info@skillet.co")
    to_email = Email("jourdesignmails@gmail.com")
    subject = "A new Feature has been Created"
    content = Content("text/plain", "Check it out on Finityboard")
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())


def gengraph(impact, effort):
    x = [effort]
    y = [impact]
    axes = plt.gca()
    axes.set_xlim([0, 10])
    axes.set_ylim([0, 10])
    plt.title('Prioritisation Matrics')
    plt.xlabel('IMPACT')
    plt.ylabel('EFFORT')
    area = 150
    plt.scatter(x, y, s=area)
    return plt.show()