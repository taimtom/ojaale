from django.urls import path
from .views import (
    user_profile,
    UserProperties
)
app_name='lessor'
urlpatterns = [
    #path('<slug>/', user_profile, name='details'),
    path('<slug>/properties/', UserProperties.as_view(), name='properties'),
]