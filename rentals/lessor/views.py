from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import DetailView,ListView,View,CreateView,UpdateView

from .forms import UserCreationForm
from properties.models import Property
# Create your views here.

def user_profile(request):
    template_name='user-profile.html'
    context={}
    return render(request,template_name,context )
class UserProperties(DetailView):
    template_name='user-properties.html'
    queryset=Property.objects.all()

class RegisterView(SuccessMessageMixin,CreateView):
	form_class=UserCreationForm
	template_name = 'registration/login.html'
	success_url = '#login'
	success_message="<tab> User successfully created, you can now Login.</tab>"
	
	def get_context_data(self,*args, **kwargs):
		context=super(RegisterView,self).get_context_data(*args,**kwargs)
		form = UserCreationForm(self.request.POST or None, self.request.FILES or None)
		context['register_form']=form
		context['title']='Sign Up'
		context['action']='register'
		return context