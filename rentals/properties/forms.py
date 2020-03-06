from django import forms

from .models import Property

class PropertyForm(forms.ModelForm):

    class Meta:
        model=Property
        fields='__all__'
        #     'name',
        #     'price',
        #     'per',
        #     'category',
        #     'location',
        #     'size',
        #     'description',
        #     'additional_features',
        #     'image',
        #     'quantity_available'
        # )
class ImageForm(forms.ModelForm):
    class Meta:
        model=Property
        fields=('images','videos')