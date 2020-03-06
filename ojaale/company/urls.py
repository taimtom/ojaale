from django.conf.urls import url
from django.urls import path



from .views import (
CompanyProfile,
companycreate_view
	)
app_name="company"
urlpatterns = [
	path('<slug>/',CompanyProfile.as_view(), name='detail'),
	path('create/form/',companycreate_view, name='create')
    
   
]