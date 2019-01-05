from django import forms
from .models import Ideas
from Products.models import myProducts

class FeaturesCreation(forms.ModelForm):
    class Meta:
        model = Ideas
        fields = (
        'iProduct','Title', 'Desciption','problems','business_reasons','impact','effort',
        'createdby','owner','area')

    def __init__(self, user, *args, **kwargs):
        super(FeaturesCreation, self).__init__(*args, **kwargs)
        self.fields['iProduct'].queryset = myProducts.objects.filter(ProductAccessList=user)

class FeaturesEdit(forms.ModelForm):
    class Meta:
        model = Ideas
        fields = (
         'iProduct', 'Title', 'Desciption', 'problems', 'business_reasons', 'impact', 'effort','owner', 'area')

    def __init__(self, user, *args, **kwargs):
        super(FeaturesEdit, self).__init__(*args, **kwargs)
        self.fields['iProduct'].queryset = myProducts.objects.filter(ProductAccessList=user)
