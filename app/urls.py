from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
#---------------------------


urlpatterns = [
    #---------------------------------App------------------------------------------------
    path('',views.home, name ='home'),
    path('about/', views.about, name ='about'),
    path('contact/', views.contact, name ='contact'),
    path('category/<slug:val>', views.Categoryview.as_view(), name = "category"),
    path('categorytitle/<val>', views.CategoryTitle.as_view(), name = "categorytitle"),
    path('detail/<int:pk>', views.Detailview.as_view(), name = "detail"),
    
    #-----------------------------------CartApp------------------------------------------
    path('addcart/',views.addcart, name='addcart'),
    path('pluscart/',views.plus_cart),
    path('minuscart/',views.minus_cart),
    path('removecart/',views.remove_cart),
    #------------------------------------------------------------------------------------
    
    path('mycart/',views.showmycart, name='showmycart'),
    path('checkout/',views.Checkout.as_view(), name='checkout'),


]+static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
