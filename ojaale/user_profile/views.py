from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.http import Http404
from django.views.generic import DetailView,ListView,View,CreateView,UpdateView

from .forms import UserCreationForm
# Create your views here.
def activate_user_view(request, code=None,*args,**kwargs):
	if code:
		qs=MyProfile.objects.filter(activation_key=code)
		if qs.exists() and qs.count()==1:
			myprofile=qs.first()
			if not myprofile.activated:
				user_=myprofile.user
				user_.is_active=True
				user_.save()
				myprofile.activated=True
				myprofile.activation_key=None

				myprofile.save()
				return redirect("/login/")
	return redirect('/login/')


class RegisterView(SuccessMessageMixin,CreateView):
	form_class=UserCreationForm
	template_name = 'registration/register.html'
	success_url = '/accounts/login/'
	success_message="<tab> User successfully created, you can now Login.</tab>"
	
	def get_context_data(self,*args, **kwargs):
		context=super(RegisterView,self).get_context_data(*args,**kwargs)
		form = UserCreationForm(self.request.POST or None, self.request.FILES or None)
		context['register_form']=form
		context['title']='Sign Up'
		context['action']='register'
		return context
    #def dispatch(self,*args,**kwargs):
    #	if self.request.user.is_authenticated():
    #		return redirect('/logout/')
    #	return super(RegisterView,self).dispatch(*args,**kwargs)
