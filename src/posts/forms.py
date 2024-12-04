from django import forms
from posts.models import Tache


class TacheForm(forms.ModelForm):
    class Meta:
        model = Tache
        fields = [
            'title', 'description', 'date_de_debut', 'date_de_fin', 'priorite', 'statut', 'avancement', 'commentaires'
        ]
        widgets = {
            'date_de_debut':forms.DateTimeInput(attrs={'type': 'date'}),
            'date_de_fin': forms.DateInput(attrs={'type': 'date'}),
        }


class TacheForm_(forms.ModelForm):
    class Meta:
        model = Tache
        fields = [
            'title', 'description', 'priorite', 'statut', 'avancement', 'commentaires'
        ]

