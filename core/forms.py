from dataclasses import fields
from django import forms
from .models import Producto

class ProductoForms(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'