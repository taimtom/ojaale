from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from .models import Cart 
from product.models import Products
User=get_user_model()

class CartToggle(LoginRequiredMixin,View):
    def post(self, request, *args, **kwargs):
        cart_=Cart.objects.filter(user__username__iexact=request.user)
        if cart_ is None:
            obj=Cart.objects.create(
            user=request.user,
            total=100
            )
            return redirect(f"/products/{product_slug}/")
        else:
            product=request.POST.get('product_name')
            instance = get_object_or_404(Products, name=product)
            request_product=instance
            product_slug=instance.slug
            username_to_toggle=request.user
            cart_,in_cart = Cart.objects.toggle_product(request_product, username_to_toggle)
            print(in_cart)
            return redirect(f"/products/{product_slug}/")
        return redirect('/accounts/login/')
	

class CartList(LoginRequiredMixin, ListView):
    template_name='main/cart/detail.html'
    def get_queryset(self):
        user=self.request.user
        qs=Cart.objects.filter(user=user)
        return qs
    
    def get_context_data(self,*args,**kwargs):
        context=super(CartList, self).get_context_data(*args, **kwargs)
        cart=self.get_queryset()
        context['cart_list']=cart
        price=0
        number_of_items=0
        for obj in cart:
            for product in obj.products.all():
                price=product.price+price
                number_of_items=number_of_items+1

        context['sub_total']=price
        context['number_of_items']=number_of_items
        print(number_of_items)

        return context