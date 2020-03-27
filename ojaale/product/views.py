from itertools import chain

from django.core.paginator import Paginator

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from urllib.parse import quote

from django.urls import reverse

from django.db.models import Q
from django.http import HttpResponseRedirect,Http404
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import View, ListView, DetailView
from django.utils import timezone

from .models import Products
from reviews.forms import ReviewForm
from reviews.models import Review
from cart.models import Cart
from .forms import ProductForm
from company.models import Company
# Create your views here.

def index(request):
	template_name="main/index_try.html"
	shops=Company.objects.all()
	products=Products.objects.all()
	cart_=get_object_or_404(Cart, user=request.user)
	context={
		"products":products,
		"shops":shops,
		'carts':cart_

	}
	return render(request, template_name, context)

class ProductsList(ListView):
	queryset=Products.objects.all()
	template_name='main/product/list.html'
	for query in queryset:
		reviews=[x.rating for x in Review.objects.filter(content_type=query.get_content_type)]
		
	
	# for review in reviews:
	# 	print(review)

	def get_context_data(self, *args, **kwargs):
		context=super(ProductsList,self).get_context_data(*args, **kwargs)
		cart_=get_object_or_404(Cart, user=self.request.user)
		context['cart']=cart_

		return context
	



def productdetail(request, slug=None):
	instance = get_object_or_404(Products, slug=slug)
	print(instance.slug)
	share_string= quote(instance.description)
	initial_data={
		"content_type":instance.get_content_type,
		"object_id":instance.id
	}
	form=ReviewForm(request.POST or None, initial=initial_data)
	if form.is_valid():
		c_type=form.cleaned_data.get("content_type")
		content_type=ContentType.objects.get(model=c_type)
		obj_id=form.cleaned_data.get("object_id")
		content_data=form.cleaned_data.get("content")
		rating=request.POST.get('rating')
		parent_obj=None
		try:
			parent_id=int(request.POST.get('parent_id'))
		except:
			parent_id=None
		if parent_id:
			parent_qs=Review.objects.filter(id=parent_id)
			if parent_qs.exists():
				parent_obj=parent_qs.first()
				print(parent_obj)
		new_review, created=Review.objects.get_or_create(
			user=request.user,
			content_type=content_type,
			object_id=obj_id,
			content=content_data,
			parent=parent_obj,
			rating=rating
			)
		return HttpResponseRedirect(new_review.content_object.get_absolute_url())
	reviews=Review.objects.filter_by_instance(instance)
	rating=[x.rating for x in reviews]
	sumrating=0
	for val in rating:
		sumrating+=val
	numberofreviews=len(rating)
	meanrating=round((sumrating/(numberofreviews)),2)


	
	
	context={
		# 'share_string':share_string,
		'object':instance,
		'reviews':reviews,
		'review_form':form,
		'meanrating':meanrating,
		'numberofreviews':numberofreviews,
		# 'product_name':instance.name,
		# 'in_cart':in_cart
		
	}
	template='main/product/detail_test.html'
	return render(request,'main/product/detail.html',context)


def productcreate_view(request):
	form = ProductForm(request.POST)
	instances=get_object_or_404(Company, owner=request.user)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.company=instances
		instance.save()
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect('/products/')
	
	if form.errors:
		print(form.errors)
		
	context={"form":form}
	template_name='main/company/form.html'