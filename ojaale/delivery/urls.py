from django.conf.urls import url
from django.urls import path



from .views import (
	checkout_view
	)
app_name="delivery"
urlpatterns = [
    path('checkout/', checkout_view, name='checkout'),
	
    
   
]