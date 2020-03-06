from django import forms
from .models import DeliveryDetails

class CheckoutForm(forms.ModelForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'First Name'}))
    class Meta:

        model=DeliveryDetails
        fields=(
            'first_name',
            'last_name',
            'company_name',
            'email',
            'country',
            'state',
            'town',
            'street',
            'number',
            'zip_code',
            'comment',

        )
        widgets={
            'first_name':forms.TextInput(attrs={'placeholder':'First Name'}),
            'last_name':forms.TextInput(attrs={'placeholder':'Last Name'}),
            'company_name':forms.TextInput(attrs={'placeholder':'Comapany Name'}),
            'email':forms.TextInput(attrs={'placeholder':'Email Name'}),
            'country':forms.TextInput(attrs={'placeholder':'Country Name'}),
            'state':forms.TextInput(attrs={'placeholder':'state Name'}),
            'town':forms.TextInput(attrs={'placeholder':'town Name'}),
            'street':forms.TextInput(attrs={'placeholder':'Street Name'}),
            'number':forms.TextInput(attrs={'placeholder':'Number'}),
            'zip_code':forms.TextInput(attrs={'placeholder':'Zip Code'}),
            'comment':forms.TextInput(attrs={'placeholder':'Comment'}),
        }


    