from django.conf.urls import url
from django.urls import path



from .views import (
CompanyProfile,
companycreate_view,
Companies
	)
app_name="company"
urlpatterns = [
	path('',Companies.as_view(), name='list'),
	path('<slug>/',CompanyProfile.as_view(), name='detail'),
	path('create/form/',companycreate_view, name='create')
    
   
]