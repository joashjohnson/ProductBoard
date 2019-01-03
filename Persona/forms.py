from django import forms
from .models import user_persona



class PersonaCreation(forms.ModelForm):
    class Meta:
        model = user_persona
        fields = (
        'PProduct','PersonaName','PersonaDescription', 'PersonaBehaviors','PersonaGoals','PFrustrationsLimitations','Picmage'
        )


class PersonaEdit(forms.ModelForm):
    class Meta:
        model = user_persona
        fields = (
        'PProduct','PersonaName','PersonaDescription', 'PersonaBehaviors','PersonaGoals','PFrustrationsLimitations','Picmage'
        )