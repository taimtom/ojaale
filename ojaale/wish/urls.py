from django.urls import path
from django.views.generic import TemplateView


from .views import WishList

app_name='wish'


urlpatterns = [
   
    path('', WishList.as_view(), name='wish'),
    
]
