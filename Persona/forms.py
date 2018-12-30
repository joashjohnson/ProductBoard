from django import forms
from .models import user_persona

class PersonaCreation(forms.ModelForm):
    class Meta:
        model = user_persona
        fields = (
        'PersonaName','PersonaDescription', 'PersonaBehaviors','PersonaGoals','PFrustrationsLimitations','Picmage'
        )
        Picmage = forms.ImageField()


class PersonaEdit(forms.ModelForm):
    class Meta:
        model = user_persona
        fields = (
        'PersonaName','PersonaDescription', 'PersonaBehaviors','PersonaGoals','PFrustrationsLimitations','Picmage'
        )