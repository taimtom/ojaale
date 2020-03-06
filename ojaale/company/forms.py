from django import forms

from .models import Company

class CompanyForm(forms.ModelForm):

    class Meta:
        model=Company
        fields=(
            'name',
            'email',
            'phone',
            'achievements',
            'description',
            'location',
            'logo',
            'product_cat',
           

        )
        widgets={
            'name':forms.TextInput(attrs={'placeholder':'Company Name'}),
            'email':forms.EmailInput(attrs={'placeholder':'Email Account'}),
            'phone':forms.TextInput(attrs={'placeholder':'Phone Number'}),
            'email':forms.TextInput(attrs={'placeholder':'Email Name'}),
            'achievements':forms.TextInput(attrs={'placeholder':'Achievements'}),
            'description':forms.TextInput(attrs={'placeholder':'Description of '}),
            'location':forms.TextInput(attrs={'placeholder':'Address of Company'}),
            'logo':forms.ClearableFileInput(attrs={'placeholder':'Logo of company'}),
            'product_cat':forms.TextInput(attrs={'placeholder':'Product Category'}),
            
        }

        