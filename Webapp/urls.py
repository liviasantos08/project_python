from django.contrib import admin
from django.urls import path, include
from pwa import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'entregas', views.EntregList, basename='entregas')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('apis/', include(router.urls)),
    path('', views.base, name='base'),
    path('product-list/', views.product_list, name='product-list'),
    path('product-create/', views.product_create, name='product-create'),
]
urlpatterns += router.urls
