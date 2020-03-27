from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from .models import Wish 
from product.models import Products
User=get_user_model()

class wishToggle(LoginRequiredMixin,View):
    def post(self, request, *args, **kwargs):
        wish_=Wish.objects.filter(user__username__iexact=request.user)
        if wish_ is None:
            obj=Wish.objects.create(
            user=request.user,
            total=0
            )
            return redirect(f"/products/{product_slug}/")
        else:
            product=request.POST.get('product_name')
            instance = get_object_or_404(Products, name=product)
            request_product=instance
            product_slug=instance.slug
            username_to_toggle=self.request.user
            wish_,in_wish = Wish.objects.toggle_product(request_product, 'theo')
            print(in_wish)
            return redirect(f"/products/{product_slug}/")
        return redirect('/accounts/login/')
	

class WishList(LoginRequiredMixin, ListView):
    template_name='main/wish/list.html'
    def get_queryset(self):
        user=self.request.user
        qs=Wish.objects.filter(user=user)
        return qs
    
    def get_context_data(self,*args,**kwargs):
        context=super(WishList, self).get_context_data(*args, **kwargs)
        wish=self.get_queryset()
        context['wish_list']=wish
        price=0
        number_of_items=0
        # for obj in wish:
        #     for product in obj.products.all():
        #         price=product.price+price
        #         number_of_items=number_of_items+1

        # print(number_of_items)

        return context