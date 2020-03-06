from .models import Review
from django import forms
 
class ReviewForm(forms.Form):
    content_type=forms.CharField(widget=forms.HiddenInput)
    object_id=forms.IntegerField(widget=forms.HiddenInput)
    #parent_id=forms.IntegerField(widget=forms.HiddenInput, required=False)
    content=forms.CharField(label="")
    