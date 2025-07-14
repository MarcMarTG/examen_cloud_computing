from django import forms
from .models import Project

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Título de tarea", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    description = forms.CharField(label="Descripción de la tarea", widget=forms.Textarea(attrs={'class': 'input'}))
    project = forms.ModelChoiceField(label="Proyecto", queryset=Project.objects.all(), empty_label="Selecciona un proyecto")
    
class CreateNewProject(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input'})
        }
