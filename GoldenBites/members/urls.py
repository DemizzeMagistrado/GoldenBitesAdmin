from django.urls import path
from . import views

urlpatterns = [
    # The root URL ('/') points to the welcome page
    path('', views.welcome_view, name='welcome_root'),
    
    # Your existing URL patterns
    path('welcome/', views.welcome_view, name='welcome'),
    path('add-item/', views.add_item_view, name='add_item'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('favorites/', views.favorites_view, name='favorites'),
    path('food-list/', views.food_list_view, name='food_list'),
    path('forgot-password/', views.forgot_password_view, name='forgot_password'),
    path('home/', views.home_view, name='home'),  # This is your home page
    path('index/', views.index_view, name='index'),
    path('landing/', views.landing_view, name='landing'),
    path('login/', views.login_view, name='login'),
    path('notifications/', views.notifications_view, name='notifications'),
    path('order-details/', views.order_details_view, name='order_details'),
    path('order-summary/', views.order_summary_view, name='order_summary'),
    path('order-tracking/', views.order_tracking_view, name='order_tracking'),
    path('orders/', views.orders_view, name='orders'),
    path('overview/', views.overview_view, name='overview'),
    path('payment/', views.payment_view, name='payment'),
    path('policy/', views.policy_view, name='policy'),
    
    # Keep ONLY this product_detail URL pattern.
    # It matches '/product-detail/' and allows query parameters like '?id=turon'
    path('product-detail/', views.product_detail_view, name='product_detail'),
    
    path('register/', views.register_view, name='register'),
    path('reset-password/', views.reset_password_view, name='reset_password'),
    path('review/', views.review_view, name='review'),
    path('sign-in/', views.sign_in_view, name='sign_in'),
    path('sign-up/', views.sign_up_view, name='sign_up'),
    # Remove this line as it's causing the error (it's a duplicate or incorrect pattern)
    # path('', views.home, name='home'),
]
