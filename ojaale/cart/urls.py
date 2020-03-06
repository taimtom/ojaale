from django.urls import path, include
from django.views.generic import TemplateView


from .views import CartList

app_name='cart'


urlpatterns = [
   
    path('', CartList.as_view(), name='cart'),
    
]
