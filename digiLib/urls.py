from django.urls import path
from .views import ProductListView, ProductCreate
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('product/new/', ProductCreate.as_view(), name='product_new')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)