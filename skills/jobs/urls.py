from django.urls import path

from .views import (
    JobList,
    JobDetail,
    job_add
    
   )
app_name='jobs'
urlpatterns = [
    path('', JobList.as_view(), name='list'),
    path('<slug>/', JobDetail.as_view(), name='detail'),
    path('create/add/', job_add, name='submit'),
   

]
