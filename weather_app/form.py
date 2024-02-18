from django.forms import ModelForm,TextInput # this is inbuld form template in django python just import after use
from .models import city

class CityForm(ModelForm):
    class Meta:
        model=city
        fields=['name']
        widgets={'name':TextInput(attrs={'class':'form-control','placeholder':'City Name'})}