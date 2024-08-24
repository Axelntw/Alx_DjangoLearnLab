from django.urls import path
from . import admin_view, librarian_view, member_view
from .views import list_books, LoginView, LogoutView, home, LibraryDetailView, home_view
from . import views


urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:book_id>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:book_id>/delete/', views.delete_book, name='delete_book'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('', home, name='home'),    
    path('admin-view/', admin_view.admin_view, name='admin_view'),
    path('librarian-view/', librarian_view.librarian_view, name='librarian_view'),
    path('member-view/', member_view.member_view, name='member_view'),
    path('', home_view, name='home'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', views.register_view, name='register'),
]