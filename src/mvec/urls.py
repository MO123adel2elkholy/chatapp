
from django.contrib import admin
from django.urls import path
from . import views
# from .views import  base
# urlpatterns = [
#     # ... the rest of your URLconf goes here ...
# ]

urlpatterns = [
    path('base', views.base, name="base"),
    path('', views.home, name="home"),
    path('product/<str:pk>', views.product_details, name="product"),
    path('page_404', views.page_404, name='page_404'),
    # path('my_account', views.my_account, name="my_account"),
    path('register', views.register, name="use_register"),
    path('login', views.user_login, name="user_login"),
    path('logout', views.user_logout, name='user_logout'),
    path('user_profile', views.user_profile, name='user_profile'),
    path('update_profile', views.update_profile, name='update_profile'),
    path('about_us', views.about_us, name='about_us'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('product', views.product, name='product'),
    path('product/filter-data', views.filter_data, name="filter-data"),
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/', views.cart_detail, name='cart_detail'),
    path('cart/checkout/', views.cart_checkout, name='checkout'),
]
