from django import forms
from .models import Ideas

class FeaturesCreation(forms.ModelForm):
    class Meta:
        model = Ideas
        fields = (
        'iProduct','Title', 'Desciption','problems','business_reasons','impact','effort',
        'createdby','owner','area')

class FeaturesEdit(forms.ModelForm):
    class Meta:
        model = Ideas
        fields = (
         'iProduct', 'Title', 'Desciption', 'problems', 'business_reasons', 'impact', 'effort','owner', 'area')


