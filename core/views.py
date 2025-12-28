
# core/views.py
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def index(request):
    return render(request, "core/index_new.html")

def root_redirect(request):
    if request.user.is_authenticated:
        return redirect('accounts:profile')
    return redirect('accounts:login')

# Custom 404 error handler
def custom_404(request, exception):
    return render(request, '404.html', status=404)
