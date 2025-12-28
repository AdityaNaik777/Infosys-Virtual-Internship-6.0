from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from .forms import RegistrationForm, UserUpdateForm

# ---------------------------
# LANDING PAGE
# ---------------------------
def index(request):
    return render(request, 'core/index.html')


# ---------------------------
# REGISTRATION
# ---------------------------
def register_view(request):
    if request.user.is_authenticated:
        return redirect('quizzes:dashboard')   # If logged in → go to dashboard

    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful! Welcome to AI Quiz Hub.")
            return redirect('quizzes:dashboard')
        else:
            # Form validation failed - errors will be displayed in template
            pass
    else:
        form = RegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})


# ---------------------------
# LOGIN VIEW (Custom Redirection)
# ---------------------------
class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True    # Prevent logged users from seeing login page

    # override success URL
    def get_success_url(self):
         return reverse_lazy('quizzes:dashboard')

# ---------------------------
# PROFILE PAGE (User model only — no UserProfile)
# ---------------------------
@login_required
def profile_view(request):
    user = request.user

    if request.method == "POST":
        if "avatar_path" in request.FILES:
            user.avatar_path = request.FILES["avatar_path"]

        user.email = request.POST.get("email", user.email)
        user.full_name = request.POST.get("full_name", user.full_name)

        user.save()
        messages.success(request, "Profile updated successfully")
        #redirect to dashboard
        return redirect("quizzes:dashboard")

    return render(request, "accounts/profile.html")



# ---------------------------
# LOGOUT
# ---------------------------
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')
