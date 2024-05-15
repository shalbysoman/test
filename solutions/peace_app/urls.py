from django.urls import path
from . import views

urlpatterns = [
    path('create-book/', views.createbook, name='create'),
    path('', views.listbook, name='list'),
    path('author/', views.create_author, name='author'),
    path('detailsview/<int:book_id>/', views.detailsbook, name='details'),
    path('updateview/<int:book_id>/', views.updatebook, name='update'),
    path('deleteview/<int:book_id>/', views.deletebook, name='delete'),
    path('index/', views.index),
    path('search/', views.search_book, name='searchview'),
]
