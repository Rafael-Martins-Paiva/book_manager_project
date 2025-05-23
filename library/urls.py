from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_management_page, name='book_management_page'),
    path('api/books/', views.books_api, name='books_api_list_create'),
    path('api/books/<str:isbn>/', views.book_detail_api, name='books_api_detail'),
]
