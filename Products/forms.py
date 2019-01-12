from django import forms
import datetime
from .models import myProducts

class ProductCreation(forms.Form):
    pName = forms.CharField(max_length=100, widget= forms.TextInput(
        attrs={'class':'form-control', 'placeholder' : 'Product Title'}))
    pDesciption = forms.CharField(widget=forms.Textarea(
        attrs={'class':'form-control', 'placeholder' : 'Product Description'}))
    pObjectives = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder' : 'Objectives'}))
    pVision = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder' : 'Vision'}))

class ProductEdit(forms.ModelForm):
    class Meta:
        model = myProducts
        fields = ('ProductTitle', 'Description','Objectives', 'Vision', 'ProductAccessList')

