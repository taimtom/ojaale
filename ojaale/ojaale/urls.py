from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import TemplateView
from cart.views import CartToggle
from user_profile.views import RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('product.urls', namespace='products')),
    path('delivery/', include('delivery.urls', namespace='delivery')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('company/', include('company.urls', namespace='company')),
    path('add_cart/', CartToggle.as_view(), name='add_cart'),
    path('register/', RegisterView.as_view(), name='register'),
    
    path('', TemplateView.as_view(template_name='test/amado/index.html'), name='home'),
    path('o/', TemplateView.as_view(template_name='main/ojaale.html'), name='ojaale'),
    path('accounts/', include('django.contrib.auth.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
