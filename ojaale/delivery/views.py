from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect,Http404
from django.contrib import messages
from .forms import CheckoutForm
from .models import DeliveryDetails

from cart.models import Cart

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
    cart_=get_object_or_404(Cart, user=request.user)
    total=0
    for product in cart_.products.all():
        price = product.price
        subtotal= price + total
    context={"form":form, 'subtotal':subtotal}
    print(form)
    template_name='main/delivery/checkout.html'
   
        
    
    return render(request, template_name,context)

 