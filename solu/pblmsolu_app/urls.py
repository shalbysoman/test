from django.urls import path
from . import views

urlpatterns = [

    path('', views.list_book, name='list'),
    path('details/<int:book_id>/', views.details_book, name='details'),
    path('search/', views.search_view, name='search'),
]
