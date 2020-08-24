from django.urls import path

from . import views

urlpatterns = [
    path('',views.cart,name="cart"),
    path('addtocart/<int:id>',views.addtocart,name="addtocart"),
    path('addrm_pro_qnt/<int:id>/<int:v>', views.addrm_pro_qut, name='addrm_pro_qut'),
    path('pro_remove/<int:id>', views.pro_remove, name='pro_remove'),
    path('checkout/',views.checkout_products,name='checkout'),
    path('checkout_shipment/',views.checkout_shipment,name='checkout_shipment'),
    path('shipment/',views.shipment,name='shipment'),
    path('shipment/<int:id>',views.shipment_id,name='shipment_id'),
]