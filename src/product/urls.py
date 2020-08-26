from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name = 'index'),
    path('product/<int:id>',views.product_view,name ="product_view"),
    path('search/',views.search,name="search"),
]