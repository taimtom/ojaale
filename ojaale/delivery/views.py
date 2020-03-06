from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404
from django.contrib import messages
from .forms import CheckoutForm
from .models import DeliveryDetails

# Create your views here.
context={}
def checkout_view(request):
    form = CheckoutForm(request.POST)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect('https://paypal.com')
        
    if form.errors:
        print(form.errors)
        context={"form":form}
    context={"form":form}
    print(form)
    template_name='main/delivery/checkout.html'
   
        
    
    return render(request, template_name,context)

 