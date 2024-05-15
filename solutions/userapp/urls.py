from django.urls import path
from . import views

urlpatterns = [

    path('', views.listbook, name='userlist'),
    path('details/<int:book_id>/', views.detailsbook, name='userdetails'),
    path('search/', views.searchview, name='search'),
]
