from django import forms
from human.models import DetailsOfHuman

class formDetails(forms.ModelForm):
    class Meta:
        model = DetailsOfHuman
        fields = ['name', 'city', 'favourite_food']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter Your Name ', 'class': 'sel1'}),
            'city': forms.TextInput(attrs={'placeholder': 'Enter Your city ', 'class': 'sel1'}),
            'favourite_food': forms.TextInput(attrs={'placeholder': 'Favourite Food', 'class': 'sel1'}),
        }
