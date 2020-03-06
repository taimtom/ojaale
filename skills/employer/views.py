from django.shortcuts import render
from django.views.generic import DetailView,ListView,View,CreateView,UpdateView

from .models import Employer

# Create your views here.
class EmployerList(ListView):
    template_name='employer-listing.html'
    queryset=Employer.objects.all()
   
class EmployerDetails(DetailView):
    template_name='employer-profile.html'
    queryset=Employer.objects.all()
def employers_favorite(request):
    template_name='employer-favorites.html'
    context={}
    return render(request,template_name,context )
def employers_transactions(request):
    template_name='employer-transactions.html'
    context={}
    return render(request,template_name,context )
def employers_submit_job(request):
    template_name='employer-submit-job.html'
    context={}
    return render(request,template_name,context )
def employers_dashboard(request):
    template_name='employer-dashboard.html'
    context={}
    return render(request,template_name,context )
def employers_change_password(request):
    template_name='employer-change-password.html'
    context={}
    return render(request,template_name,context )