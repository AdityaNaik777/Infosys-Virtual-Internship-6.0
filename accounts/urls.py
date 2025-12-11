# accounts/urls.py

from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

# Use a specific list of password reset views from django.contrib.auth
# to avoid conflicts with your custom login/logout views.
auth_urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(), name='login'), # We define this custom below
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'), # We define this custom below
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]


urlpatterns = [
    # 1. Custom User Views
    path('register/', views.register_view, name='register'),
    
    # Use your CustomLoginView defined in views.py
    path('login/', views.CustomLoginView.as_view(
        template_name='accounts/login.html',
        next_page='quizzes:dashboard' # Redirects here on success
    ), name='login'),
    
    # Use your custom logout view (defined in views.py)
    path('logout/', views.logout_view, name='logout'),
    
    path('profile/', views.profile_view, name='profile'),
    
    # 2. Quizzes App Inclusion (This is likely wrong. See note below)
    # path("quiz/", include("quizzes.urls")), 
    
    # 3. Django Auth URLs (Password Reset)
    # Includes only the password reset logic, prefixed under /accounts/
    path('', include(auth_urlpatterns)), 
]