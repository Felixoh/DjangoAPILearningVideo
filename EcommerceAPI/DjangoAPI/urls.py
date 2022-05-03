from django.urls import path 
from .views import *

urlpatterns = [
    #categories api endpoints
    path('categories',ListCategory.as_view(),name='categories'),
    path('categories/<int:pk>/',DetailCategory.as_view(),name='singlecategory'),

    #Django books API paths and libraries:
    path('books',ListBook.as_view(),name='books'),
    path('books/<int:pk>/',DetailBook.as_view(),name="singlebook"),

    #products api endpoints:
    path('products',ListProduct.as_view(),name='products'),
    path('products/<int:pk>/',DetailProduct.as_view(),name='singleproduct')
]
