from django import forms
from .models import Project


class ProjectCreateForm(forms.ModelForm):
    class Meta():
        model = Project
        fields = ['name', 'budget']
        widgets= {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'budget': forms.NumberInput(attrs={'class':'form-control'}),
        }

class ExpenseForm(forms.Form):
    title = forms.CharField()
    amount = forms.IntegerField()
    category = forms.CharField()
