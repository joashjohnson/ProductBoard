from django import forms
from .models import user_persona
from Products.models import myProducts


class PersonaCreation(forms.ModelForm):
    class Meta:
        model = user_persona
        fields = (
        'PProduct','PersonaName','PersonaDescription', 'PersonaBehaviors','PersonaGoals','PFrustrationsLimitations','Picmage'
        )

    def __init__(self, user, *args, **kwargs):
        super(PersonaCreation, self).__init__(*args, **kwargs)
        self.fields['PProduct'].queryset = myProducts.objects.filter(ProductAccessList=user)


class PersonaEdit(forms.ModelForm):
    class Meta:
        model = user_persona
        fields = (
        'PProduct','PersonaName','PersonaDescription', 'PersonaBehaviors','PersonaGoals','PFrustrationsLimitations','Picmage'
        )

    def __init__(self, user, *args, **kwargs):
        super(PersonaEdit, self).__init__(*args, **kwargs)
        self.fields['PProduct'].queryset = myProducts.objects.filter(ProductAccessList=user)