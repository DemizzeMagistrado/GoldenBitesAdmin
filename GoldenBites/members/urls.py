"""
URL configuration for goldenbites project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# members/urls.py
from django.urls import path
from . import views # . means from the current package/app

urlpatterns = [
    path('', views.welcome_view, name='welcome'), # For your main landing page if it exists
    path('sign-in/', views.sign_in_view, name='sign_in'), # This is the crucial line for sign-in
    path('sign-up/', views.sign_up_view, name='sign_up'), # As seen in previous context
    path('policy/', views.policy_view, name='policy'), # As seen in previous context
    path('policy-admin/', views.policy_admin_view, name='policy_admin'),
    path('favorites/', views.favorites_view, name='favorites'),
    path('food-list/', views.food_list_view, name='food_list'),
    path('forgot-password/', views.forgot_password_view, name='forgot_password'),
    path('home/', views.home_view, name='home'),
    path('login/', views.login_view, name='login'), # If different from sign-in
    path('notifications/', views.notifications_view, name='notifications'),
    path('order-details/', views.order_details_view, name='order_details'),
    path('order-summary/', views.order_summary_view, name='order_summary'),
    path('order-tracking/', views.order_tracking_view, name='order_tracking'),
    path('orders/', views.orders_view, name='orders'),
    path('overview/', views.overview_view, name='overview'),
    path('payment/', views.payment_view, name='payment'),
    path('product-detail/', views.product_detail_view, name='product_detail'),
    path('register/', views.register_view, name='register'), # If different from sign-up
    path('reset-password/', views.reset_password_view, name='reset_password_confirm'),
    path('review/', views.review_view, name='review'),
    path('landing/', views.landing_view, name='landing'),
    path('customer-sign-up/', views.customer_sign_up_view, name='customer_sign_up'),
     path('dashboard/', views.dashboard_view, name='dashboard'),
    path('add-item/', views.add_item_view, name='add-item')
]
