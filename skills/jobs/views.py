from django.shortcuts import render
from django.views.generic import DetailView,ListView,View,CreateView,UpdateView

from .models import Job
from .forms import JobForm
# Create your views here.
class JobList(ListView):
    template_name='job-search.html'
    def get_queryset(self):
        queryset=Job.objects.all()
        query=self.request.GET.get('search')
        if query:
            query=query.strip()
            queryset=queryset.search(query)
        return queryset
class JobDetail(DetailView):
    template_name='job-single.html'
    queryset=Job.objects.all()
def job_add(request):
    template_name='job-add.html'
    form = JobForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.owner=request.user
        instance.save()
        #messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context={
    "form":form
    }
    return render(request, template_name, context)
