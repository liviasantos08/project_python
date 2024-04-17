from django.forms import NumberInput
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    data_compra = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))

    class Meta:
        model = Product
        fields = ['name', 'description', 'price','data_compra']


