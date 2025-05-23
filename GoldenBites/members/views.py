from django.shortcuts import render

def add_item_view(request):
    return render(request, 'add-item.html')

def dashboard_view(request):
    return render(request, 'dashboard.html')

def favorites_view(request):
    return render(request, 'favorites.html')

def food_list_view(request):
    return render(request, 'food-list.html')

def forgot_password_view(request):
    return render(request, 'forgot-password.html')

def home_view(request):
    return render(request, 'home.html')

def index_view(request):
    return render(request, 'index.html')

def login_view(request):
    return render(request, 'login.html')

def notifications_view(request):
    return render(request, 'notifications.html')

def order_details_view(request):
    return render(request, 'order-details.html')

def order_summary_view(request):
    return render(request, 'order-summary.html')

def order_tracking_view(request):
    return render(request, 'order-tracking.html')

def orders_view(request):
    return render(request, 'orders.html')

def overview_view(request):
    return render(request, 'overview.html')

def payment_view(request):
    return render(request, 'payment.html')

def policy_view(request):
    return render(request, 'policy.html')

# This is the correct product_detail_view, as product-detail.html expects 'id' via query parameter
def product_detail_view(request):
    # Your product-detail.html's JavaScript already handles fetching the product data
    # based on the 'id' query parameter. So, this view simply needs to render the template.
    return render(request, 'product-detail.html')

def register_view(request):
    return render(request, 'register.html')

def reset_password_view(request):
    return render(request, 'reset-password.html')

def review_view(request):
    return render(request, 'review.html')

def sign_in_view(request):
    return render(request, 'sign-in.html')

def sign_up_view(request):
    return render(request, 'sign-up.html')

def welcome_view(request):
    return render(request, 'welcome.html')

def landing_view(request):
    # Your landing page view logic here
    return render(request, 'landing.html')

def customer_sign_up_view(request):
    # Your customer sign-up view logic here
    return render(request, 'customer/sign-up.html')
