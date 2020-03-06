from django.shortcuts import render,get_object_or_404
from django.views.generic import View, ListView, DetailView, CreateView
from django.forms import formset_factory
from .models import Property
from .forms import PropertyForm, ImageForm
from lessor.models import Lessor
# Create your views here.
def index(request):
    template_name='index.html'
    context={}
    return render(request,template_name,context )
class PropertyDetail(DetailView):
    template_name='props.html'
    queryset=Property.objects.all()
    # def get_context_data(self,*args,**kwargs):
    #     context=super(PropertyDetail,self).get_context_data(*args, **kwargs)
    #     qs=Property.objects.filter(lessor=queryset.lessor)
    #     context['lessor_prop']=qs
    #     return context
class Properties(ListView):
    template_name='properties.html'
    def get_queryset(self):
        query=self.request.GET.get('search')
        queryset=Property.objects.all()
        if query:
            query=query.strip()
            queryset = queryset.search(query)
        return queryset
    def get_context_data(self,*args,**kwargs):
        context=super(Properties,self).get_context_data(*args,**kwargs)
        query=self.request.GET.get('search')
        context['query']=query
        return context
    

def submit_property(request):
    #image_form=formset_factory(ImageForm, extra =2)
    form = PropertyForm(request.POST,request.FILES)
    #category=request.POST.get('category')
    #size=request.POST.get('size')
    lessor_instance=get_object_or_404(Lessor, owner=request.user)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.lessor=lessor_instance
        #instance.category=category
        #instance.size=size
        instance.save()
        #messages.success(request, "Successfully Created")
        return HttpResponseRedirect(f'/properties/{instance.slug}')
        
    if form.errors:
        print(form.errors)
        context={"form_error":form.errors}
    context={"form":form}
    template_name='submit-property.html'

    return render(request, template_name,context)
