from django.urls import path
from .views import *

urlpatterns=[
    path('',home,name='home'),
    path('cart',cart,name='cart'),
    path('profile',profile,name='profile'),
    path('updateprofile|<int:id>',updateprofile,name='updateprofile'),
    path('changepassword|<int:id>',changepassword,name='changepassword'),
    path('deleteaccount|<int:id>',deleteaccount,name='deleteaccount'),
    path('addcart|<int:id>',addcart,name='addcart'),
    path('quantityminus|<int:id>',quantityminus,name='quantityminus'),
    path('quantityplus|<int:id>',quantityplus,name='quantityplus'),
    path('remove|<int:id>',remove,name='remove'),
    path('contactus',contactus,name='contactus'),
    path('checkout',checkout,name='checkout'),
    path('count',count_,name='count'),
    path('aboutus',aboutus,name='aboutus'),
    path('orderplaced',orderplaced,name='orderplaced')
]