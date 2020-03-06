from django.urls import path
from .views import (
    PropertyDetail,
    Properties,
    submit_property
  
)
app_name='properties'
urlpatterns = [
    path('<slug>/', PropertyDetail.as_view(), name='detail'),
    path('', Properties.as_view(), name='list'),
    path('submit/creates/', submit_property, name='submit'),
   
]