from django.urls import path
from . import views

urlpatterns = [

    path('', views.listbook, name='userlist'),
    path('details/<int:book_id>/', views.detailsbook, name='userdetails'),
    path('search/', views.searchview, name='search'),
    path('add_to_cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    # path('view-cart/', views.view_cart, name='view_cart'),
    path('increase/<int:item_id>/', views.increase_quantity, name='increase_quantity'),
    path('decrease/<int:item_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_cart'),
    path('viewcart/', views.viewcart, name='viewcart'),
]
