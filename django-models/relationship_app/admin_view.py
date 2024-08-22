# admin_view.py
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied

def is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'Admin'

@user_passes_test(is_admin, login_url='/login/')
def admin_dashboard(request):
    # This view will only be accessible to users with the 'Admin' role
    return render(request, 'admin_dashboard.html')
