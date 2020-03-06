from django.urls import path

from .views import (
    EmployerList,
    EmployerDetails,
    employers_favorite,
    employers_transactions,
    employers_submit_job,
    employers_dashboard,
    employers_change_password


   )
app_name='employer'
urlpatterns = [
    path('', EmployerList.as_view(), name='list'),
    path('<slug>/', EmployerDetails.as_view(), name='detail'),
    path('favorites/', employers_favorite, name='job_add'),
    path('transactions/', employers_transactions, name='transactions'),
    path('create/add/', employers_dashboard, name='update'),
    path('password-update', employers_change_password, name='update_password'),
   

]
