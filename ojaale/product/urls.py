from django.conf.urls import url
from django.urls import path



from .views import (
	ProductsList,
	productdetail,
	productcreate_view
    

	)
app_name="products"
urlpatterns = [
    path('', ProductsList.as_view(), name='list'),
	
	path('<slug>/',productdetail, name='detail'),
	path ('create/form/', productcreate_view, name='create')
	#ProductsDetail.as_view(), name='detail'),
    
   
]