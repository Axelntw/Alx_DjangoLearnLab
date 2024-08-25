from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.db.models import Q
from .models import Book
from .forms import BookSearchForm

def book_search(request):
    if request.method == 'POST':
        form = BookSearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
    else:
        form = BookSearchForm()
        books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'form': form, 'books': books})
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        if title and author:
            Book.objects.create(title=title, author=author)
            return redirect('book_list')
    return render(request, 'bookshelf/add_book.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title', book.title)
        book.author = request.POST.get('author', book.author)
        book.save()
        return redirect('book_list')
    return render(request, 'bookshelf/edit_book.html', {'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/delete_book.html', {'book': book})
