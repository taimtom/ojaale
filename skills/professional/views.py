from django.shortcuts import render,get_object_or_404
from django.views.generic import DetailView,ListView,View,CreateView,UpdateView
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect,Http404

from .models import Professional
from .models import Testimony
from .forms import ProfessionalForm
from .models import Job
from review.forms import ReviewForm
from review.models import Review

# Create your views here.
def index(request):
    template_name='index.html'
    jobs=Job.objects.all()
    testimonies=Testimony.objects.all()
    professionals=Professional.objects.all()
    context={
        'jobs':jobs,
        'testimonies':testimonies,
        'professionals':professionals
    }
    return render(request,template_name,context )
class ProfessionalList(ListView):
    template_name='freelancer-search.html'
    def get_queryset(self):
        queryset=Professional.objects.all()
        query=self.request.GET.get('search')
        loc_query=self.request.GET.get('locate')
        profes_query=self.request.GET.get('search')
        if query and loc_query:
            query=query.strip()
            loc_query=loc_query.strip()
            queryset=queryset.search(query,loc_query)
        return queryset
    
def professionals_resume(request, slug=None):
    template_name='freelancer-edit-resume.html'
    form=ProfessionalForm(request.POST)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.save()
    context={'form':form}
    return render(request,template_name,context )
def professionals_dashboard_edit(request, slug=None):
    template_name='freelancer-dashboard.html'
    form=ProfessionalForm(request.POST)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.save()
    context={'form':form}
    return render(request,template_name,context )
    context={}
    return render(request,template_name,context )
class ProfessionalDetail(DetailView):
    template_name='freelancer-profile.html'
    def get_object(self):
        slug= self.kwargs.get("slug")
        if slug is None:
            raise Http404
        return get_object_or_404(Professional,slug__iexact=slug)
    def get_context_data(self,*args,**kwargs):
        context=super(ProfessionalDetail,self).get_context_data(*args,**kwargs)
        # slug=self.get_object()
        # instance = get_object_or_404(Professional, slug=slug)
        instance=self.get_object()
        initial_data={
            
            "content_type":instance.get_content_type,
            "object_id":instance.id
        }
        form=ReviewForm(self.request.POST or None, initial=initial_data)
        if form.is_valid():
            c_type=form.cleaned_data.get("content_type")
            content_type=ContentType.objects.get(model=c_type)
            obj_id=form.cleaned_data.get("object_id")
            content_data=form.cleaned_data.get("content")
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
            new_Review, created=Review.objects.get_or_create(

                user=request.user,
                content_type=content_type,
                object_id=obj_id,
                content=content_data,
                parent=parent_obj
                )
            return HttpResponseRedirect(new_Review.content_object.get_absolute_url())

        reviews=Review.objects.filter_by_instance(instance)
        
        context={
            'object':instance,
            'reviews':reviews,
            'review_form':form
        }
        return context
    
def professionals_active_jobs(request, slug=None):
    template_name='freelancer-active-jobs.html'
    context={}
    return render(request,template_name,context )
def job_completed(request, slug=None):
    template_name='freelancer-passed-jobs.html'
    context={}
    return render(request,template_name,context )
def change_password(request, slug=None):
    template_name='freelancer-change-password.html'
    context={}
    return render(request,template_name,context )