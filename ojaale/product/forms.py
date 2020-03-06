from django import forms
from .models import Products

class ProductForm(forms.ModelForm):
    
    class Meta:

        model=Products
        fields=(
            'name',
            'category',
            'sub_category',
            'price',
            'discounted_from',
            'availability',
            'brand',
            'size',
            'description',
            'color',
            'image',

        )
        widgets={
            'name':forms.TextInput(attrs={'placeholder':'Product Name'}),
            'category':forms.TextInput(attrs={'placeholder':'Category'}),
            'sub_category':forms.TextInput(attrs={'placeholder':'Sub Category'}),
            'price':forms.TextInput(attrs={'placeholder':'Price'}),
            'discounted_from':forms.TextInput(attrs={'placeholder':'Former Price'}),
            'availability':forms.TextInput(attrs={'placeholder':'Availability'}),
            'brand':forms.TextInput(attrs={'placeholder':'Brand'}),
            'size':forms.TextInput(attrs={'placeholder':'Size'}),
            'description':forms.TextInput(attrs={'placeholder':'Description'}),
            'color':forms.TextInput(attrs={'placeholder':'Color'}),
            'image':forms.ClearableFileInput(attrs={'placeholder':'Image'}),
        }


    