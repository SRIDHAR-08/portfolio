from django.urls import path
from .views import *


urlpatterns = [
    path('e_commerce/',home_page,name='e_commerce_home'),
    path('e_commerce/register/', register, name='e_commerce_register'),
    path('e_commerce/category/', category, name='e_commerce_category'),
    path('e_commerce/Cart/', Cart, name='e_commerce_Cart'),
    path('e_commerce/category/<int:id>/', collectionview, name='e_commerce_collectionview'),
    path('e_commerce/favourite/', favourite, name='e_commerce_favourite'),
]

