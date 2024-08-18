# admin_view.py
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied

def is_admin(user):
    if user.is_authenticated and user.userprofile.role == 'Admin':
        return True
    raise PermissionDenied

@user_passes_test(is_admin, login_url='/login/')
def admin_view(request):
    return render(request, 'admin_view.html')
