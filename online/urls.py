from django.urls import path
from online import views
from django.conf import settings
from django.conf.urls.static import static
app_name='online'
urlpatterns=[
    path('item/',views.itemsview, name="itemsview"),
    path('product/',views.productview, name="productview"),
    path('details/',views.productdetails, name="productdetails"),
    path('modify/<pk>/',views.productmodify, name="productmodify"),
    path('delete/<pk>/',views.productdelete, name="productdelete"),
    
] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)