from django.shortcuts import render,get_object_or_404
from django.views.generic import View, ListView, DetailView, CreateView
from .models import Company
from product.models import Products
from django.http import HttpResponseRedirect,Http404
from django.contrib import messages
from .forms import CompanyForm
# Create your views here.

class CompanyProfile(DetailView):
   
   queryset=Company.objects.all()

   def get(self,request, slug=None, *args, **kwargs):
      instance=get_object_or_404(Company, slug=slug)
      products=Products.objects.filter(company=instance)
      fashion=False
      if instance.product_cat=='fashion':
         fashion=True
      elif instance.product_cat=='agric':
         agric=True
      elif instance.product_cat=='technology':
         technology=True
      if instance.product_cat=='children':
         children=True
      else:
         others=True
      template_name='main/company/profile.html'
      context={
         'fashion':fashion,
         'object':instance,
         'products':products,
      }
      return render(request,template_name, context)
def companycreate_view(request):
    form = CompanyForm(request.POST)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.owner=request.user
        instance.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(f'/company/{instance.slug}')
        
    if form.errors:
        print(form.errors)
        context={"form":form}
    context={"form":form}
    print(form)
    template_name='main/company/form.html'
   
        
    
    return render(request, template_name,context)

 