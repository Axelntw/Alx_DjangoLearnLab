from django.urls import path
from . import admin_view, librarian_view, member_view
from .views import list_books, login_view, logout_view, register, home, LibraryDetailView  


urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    path('', home, name='home'),
    path('admin-view/', admin_view.admin_view, name='admin_view'),
    path('librarian-view/', librarian_view.librarian_view, name='librarian_view'),
    path('member-view/', member_view.member_view, name='member_view'),
]