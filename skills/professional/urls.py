from django.urls import path

from .views import (
    ProfessionalList,
    professionals_resume,
    professionals_dashboard_edit,
    ProfessionalDetail,
    professionals_active_jobs,
    job_completed,
    change_password)
app_name='professional'
urlpatterns = [
    path('', ProfessionalList.as_view(), name='list'),
    path('<slug>/resume/', professionals_resume, name='resume'),
    path('<slug>/dashboard/', professionals_dashboard_edit, name='dashboard'),
    path('<slug>/', ProfessionalDetail.as_view(), name='detail'),
    path('<slug>/jobs/', professionals_active_jobs, name='jobs'),
    path('<slug>/completed/', job_completed, name='completed'),
    path('<slug>/reset-password/', change_password, name='reset_password'),

]
