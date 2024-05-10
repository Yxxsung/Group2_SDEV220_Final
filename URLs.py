from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
	path('', views.product_list, name='product_list'),
	path('/home', views.home, name='home'),
	path('cart/', views.view_cart, name='view_cart'),
	path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
	path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]

#it still says to Add the necessary URL patterns for serving media files in your project’s urls.py which I believe is:
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('cart.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
